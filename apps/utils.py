from django.contrib.auth.models import User, Group
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

def register_cap_users(user):
    membership_agremiado = Membership.objects.get(membership_type='PLPA')
    membership_noagremiado = Membership.objects.get(membership_type='PNA')

    cap_num=user['cap']
    is_member = APIMember.objects.filter(cap_num=cap_num).exists()

    if is_member:
        obj = APIMember.objects.get(cap_num=user['cap'])
        is_enabled = obj.is_enabled
        penalty_fee = obj.penalty_fee
        if is_enabled and not penalty_fee:
            #users able to free account acording to ERP
            member, created = Member.objects.get_or_create(
                            names= obj.name_user,
                            first_surname= obj.first_surname, 
                            second_surname= obj.second_surname, 
                            identity= obj.identity, 
                            person_type= obj.person_type, 
                            mobile= obj.mobile, 
                            phone= obj.phone, 
                            email= user['email'], 
                            address= obj.address, 
                            profession= obj.profession, 
                            tuition= user['cap'], 
                            secret_code= obj.secret_code,
                            membership= membership_agremiado,
                            is_enabled= True,
                            penalty_fee= False,
                            has_tutition= True
                            )
            print('.............................')
            print(member)
            password = user['password1']

            #group = Group.objects.get(name='Gratuito')      
            user = User.objects.create_user(member.tuition, member.email, password)
            user.last_name = member.first_surname
            #user.groups.add(group)
            user.save()
            #update member according to user created above
            m=Member.objects.get(id=member.id)
            m.user=user
            m.save()
            return member
        else:
            #users that not are abled to free account PLPA
            member, created=Member.objects.get_or_create(
                            names= obj.name_user,
                            first_surname= obj.first_surname, 
                            second_surname= obj.second_surname, 
                            identity= obj.identity, 
                            person_type= obj.person_type, 
                            mobile= obj.mobile, 
                            phone= obj.phone, 
                            email= user['email'], 
                            address= obj.address, 
                            profession= obj.profession, 
                            tuition= user['cap'], 
                            secret_code= obj.secret_code,
                            membership= membership_noagremiado,
                            is_enabled= False,
                            penalty_fee= True,
                            has_tutition= False
                            )
            
            password = user['password1']
            #group = Group.objects.get(name='Gratuito')      
            user = User.objects.create_user(member.tuition, member.email, password)
            user.last_name = member.first_surname
            #user.groups.add(group)
            user.save()
            #update member according to user created above
            m=Member.objects.get(id=member.id)
            m.user=user
            m.save()
            return member

def register_external_user(user):
    membership_noagremiado = Membership.objects.get(membership_type='PNA')
    member, created = Member.objects.get_or_create(
                            names= user['names'],
                            first_surname= user['first_surname'], 
                            second_surname= user['second_surname'], 
                            identity= user['identity'], 
                            mobile= user['mobile'],
                            phone= user['phone'], 
                            email= user['email'], 
                            address= user['address'], 
                            tuition= user['identity'], 
                            membership= membership_noagremiado
                            )
    print('====================================')
    print(member.names)
    password = user['password1']
    #group = Group.objects.get(name='Gratuito')      
    user = User.objects.create_user(member.tuition, member.email, password)
    user.last_name = member.first_surname
    #user.groups.add(group)
    user.save()
    #update member according to user created above
    m=Member.objects.get(id=member.id)
    m.user=user
    m.save()
    return member