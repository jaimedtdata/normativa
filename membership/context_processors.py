from apps.models import Member


def membership_type(request):
    membership= None
    try:
        member= Member.objects.get(id=request.user.id)
        if member.membership.membership_type == 'PNA':
            membership = 'Plan no Agremiado'
        elif member.membership.membership_type == 'PLPA':
            membership = 'Pago en Linea - Plan Agremiado'
        elif member.membership.membership_type == 'PLPPA':
            membership = 'Pago en Linea - Plan Premium Agremiado'
        elif member.membership.membership_type == 'PLPP':
            membership = 'Pago en Linea - Plan Profesional'
        elif member.membership.membership_type == 'PPPA':
            membership = 'Pagos Presenciales - Plan Agremiado'
        elif member.membership.membership_type == 'PPPPA':
            membership = 'Pagos Presenciales - Plan Premium Agremiadoo'
        elif member.membership.membership_type == 'PPPP':
            membership = 'Pagos Presenciales - Plan Profesional'

        print(member.membership.membership_type)

        context = {'membership':membership}
        return context
    except:
        return {}
    
