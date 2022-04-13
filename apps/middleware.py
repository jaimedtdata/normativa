from django.utils import timezone
from datetime import date
from apps.models import Order_payment
from apps.models import Membership, Member
from membership.models import APIMember
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
class CheckMembership:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        #Activar o desactivar usuarios profesionales dependiendo si han pagado.
        if User.objects.exists():
                for user in User.objects.filter(is_active=False):
                    if user.is_active ==False:
                        type_membership = user.user_membership.membership.membership_type
                        if type_membership == 'PLPP':
                            orders_exists = Order_payment.objects.filter(identity=user.user_membership.identity).exists()
                            if orders_exists:
                                last_order = Order_payment.objects.filter(identity=user.user_membership.identity).latest('created')
                                day_finish_plan = last_order.validity_date_finish
                                actual_day = timezone.now()
                                if actual_day > day_finish_plan:
                                    # pasa a usuario inactivo
                                    user.is_active = False
                                    user.save()
                                else:
                                #debe ser usuario activo 
                                    user.is_active = True
                                    user.save()

                        if  type_membership == 'PPPP':
                            #profesional plan pago presencial
                            pro_usuario = APIMember.objects.get(identity=user.username)
                            actual_day = timezone.now()
                            if pro_usuario.date_expired > actual_day:
                                user.is_active = True  
                                user.save()
                                
       
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

            elif type_membership=='PLPP' :
                #profesional plan pago en linea
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
                        user.is_active = True
                        user.save()
                        
                       
                else:
                    user.is_active = False
                    user.save()
                    logout(request)
                    return redirect('login')
            
            elif type_membership=='PPPP' :
                #profesional plan pago presencial
                pro_usuario = APIMember.objects.get(identity=request.user.username)
                actual_day = timezone.now()
                if pro_usuario.date_expired > actual_day:
                    print("tienes membresia activa")
                else:
                    print("no debes tener membresia")
                    user.is_active = False  
                    user.save()
                    logout(request)
                    return redirect('login')
                
                
                            
        except:
            #print('eres super user U otro tipo de usuario ')
            pass
            
                     
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response