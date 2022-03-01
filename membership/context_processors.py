from apps.models import Member

def membership_type(request):
    # try:
    #     type_membership = Member.objects.get(tuition=request.user.username).membership
    #     print(type_membership)

    #     return {'membership':type_membership}
    # except:
    #     return {}
    ##########

    try:
        type_membership = Member.objects.get(tuition=request.user.username).membership.membership_type
        print(type_membership)
        #type_membership = request.user.user_membership.membership
        if type_membership == 'PNA' :
            membership = 'Plan no Agremiado'
        elif type_membership == 'PLPA':
            membership = 'Pago en Linea - Plan Agremiado'
        elif type_membership == 'PLPPA':
            membership = 'Pago en Linea - Plan Premium Agremiado'
        elif type_membership == 'PLPP':
            membership = 'Pago en Linea - Plan Profesional'
        elif type_membership == 'PPPA':
            membership = 'Pagos Presenciales - Plan Agremiado'
        elif type_membership == 'PPPPA':
            membership = 'Pagos Presenciales - Plan Premium Agremiadoo'
        elif type_membership == 'PPPP':
            membership = 'Pagos Presenciales - Plan Profesional'

        
        return {'membership': membership}
    except:
        return {}
    
