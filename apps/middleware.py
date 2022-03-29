from django.utils import timezone
from datetime import date
from apps.models import Order_payment
from apps.models import Membership, Member
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
class CheckMembership:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        
        try:
            user = User.objects.get(username=request.user.username)
            type_membership = user.user_membership.membership.membership_type
            #exclude super users
            print("usuario premium agremiado", type_membership=='PLPPA')
            print("usuario agremiado",type_membership=='PLPA')
            identity = user.user_membership.identity
            member = Member.objects.get(identity=identity)
            orders_exists = Order_payment.objects.filter(identity=identity).exists()

            if type_membership=='PLPA' or type_membership=='PLPPA' :
                if orders_exists:
                    last_order = Order_payment.objects.filter(identity=identity).latest('created')
                    day_finish_plan = last_order.validity_date_finish
                    actual_day = timezone.now()
                    if actual_day > day_finish_plan:
                        # regresar a plan agremiado
                        pl_agremiado=Membership.objects.get(membership_type='PLPA')
                        member.membership = pl_agremiado
                        member.save()
                    else:
                        #actualizar membresia a Premium
                        premium_agremiado=Membership.objects.get(membership_type='PLPPA')
                        member.membership = premium_agremiado
                        member.save()
                else:
                    # regresar a plan agremiado
                    pl_agremiado=Membership.objects.get(membership_type='PLPA')
                    member.membership = pl_agremiado
                    member.save()

            elif type_membership=='PLPP' or type_membership=='PPPP' :
                #profesional plan
                print('usuario:', user.is_active)

                if orders_exists:
                    last_order = Order_payment.objects.filter(identity=identity).latest('created')
                    day_finish_plan = last_order.validity_date_finish
                    actual_day = timezone.now()
                    if actual_day > day_finish_plan:
                        # pierde acceso
                        user.is_active = False
                        user.save()
                        logout(request)
                        return redirect('login')
                    else:
                        #mantener membresia profesional
                        pl_profesional=Membership.objects.get(membership_type='PLPP')
                        member.membership = pl_profesional
                        member.save()
                       
                else:
                    # no debe tener acceso
                    user.is_active = False
                    user.save()
                    logout(request)
                    return redirect('login')
                        
                            
        except:
            print('eres super user U otro tipo de usuario ')
        
                     
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response