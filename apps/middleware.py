from django.utils import timezone
from datetime import date
from apps.models import Order_payment
from apps.models import Membership, Member
from django.contrib.auth.models import User

class CheckMembership:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        
        try:
            user = User.objects.get(username=request.user.username)
            if user.user_membership:
                print('usuario agremiado', user.user_membership)
                identity = user.user_membership.identity
                member = Member.objects.get(identity=identity)
                print("identidad del usuario", user)
                orders_exists = Order_payment.objects.filter(identity=identity).exists()
                orders = Order_payment.objects.filter(identity=identity)
                if orders_exists:
                    for order in orders:
                        if order.validity_date_finish > date.today():
                            #print('actualizar membresia')
                            #actualizar membresia a Premium
                            premium_agremiado=Membership.objects.get(membership_type='PLPPA')

                            member.membership = premium_agremiado
                            member.save()
                            
                else:
                    pl_agremiado=Membership.objects.get(membership_type='PLPA')
                    member.membership = pl_agremiado
                    member.save()
                    #actualizar mebresia a Agremiado
                    pass
        except:
            print('eres super user')
        
                     
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response