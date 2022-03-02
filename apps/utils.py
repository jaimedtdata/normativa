from membership.models import APIMember, Membership
from .models import Member


def create_member_free(user):
    membership_agremiado = Membership.objects.get(membership_type='PLPA')
    membership_noagremiado = Membership.objects.get(membership_type='PNA')

    cap_num=user['tuition']
    is_member = APIMember.objects.filter(cap_num=cap_num).exists()

    if is_member:
        obj = APIMember.objects.get(cap_num=cap_num)
        is_enabled = obj.is_enabled
        penalty_fee = obj.penalty_fee
        if is_enabled and not penalty_fee:
            #users able to free account acording to ERP
            member, created = Member.objects.get_or_create(
                            names= user['names'],
                            first_surname= user['first_surname'], 
                            second_surname= user['second_surname'], 
                            identity= user['identity'], 
                            person_type= user['person_type'], 
                            mobile= user['mobile'], 
                            phone= user['phone'], 
                            email= user['email'], 
                            address= user['address'], 
                            profession= user['profession'], 
                            tuition= user['tuition'], 
                            secret_code= user['secret_code'],
                            membership= membership_agremiado,
                            is_enabled= True,
                            penalty_fee= False,
                            has_tutition= True
                            )
            print('.............................')
            print(member)
            return member
        else:
            #users that not are abled to free account PLPA
            member, created=Member.objects.get_or_create(
                            names= user['names'],
                            first_surname= user['first_surname'], 
                            second_surname= user['second_surname'], 
                            identity= user['identity'], 
                            person_type= user['person_type'], 
                            mobile= user['mobile'], 
                            phone= user['phone'], 
                            email= user['email'], 
                            address= user['address'], 
                            profession= user['profession'], 
                            tuition= user['tuition'], 
                            secret_code= user['secret_code'],
                            membership= membership_noagremiado,
                            is_enabled= False,
                            penalty_fee= True,
                            has_tutition= False
                            )
            return member
    else:
        #external Users that can be other professionals
        member, created = Member.objects.get_or_create(
                            names= user['names'],
                            first_surname= user['first_surname'], 
                            second_surname= user['second_surname'], 
                            identity= user['identity'], 
                            person_type= user['person_type'], 
                            mobile= user['mobile'], 
                            phone= user['phone'], 
                            email= user['email'], 
                            address= user['address'], 
                            profession= user['profession'], 
                            tuition= user['identity'], 
                            secret_code= user['secret_code'],
                            membership= membership_noagremiado
                            )
        print('====================================')
        print(member.names)
        return member