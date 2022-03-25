import json
import uuid
import random
import datetime
from django.utils import timezone
from django.core.paginator import Paginator
from datetime import datetime
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from apps.email import (send_confirm_account, send_success_sign_up,
    send_password_reset, send_success_password_reset,)

from django.views.generic import CreateView, FormView, TemplateView
from django.urls import reverse, reverse_lazy
from apps.forms import ( SignUpForm ,LiquidForm, SessionFormset, ComisionForm,PlanForm,
                CommentForm,  ArquitectFormset, EntrevistaFormset, EntrevistaForm, MUNI_CHOICES,
                PROVINCE_CHOICES, RulesForm, UserLoginForm, ExternalRegisterForm)
from apps.choices import (AREAS_CHOICES, PUESTOS_CHOICES,
                               works_list, get_themes, SANCTIONS_CATEGORIES, PREVENTIONS_CHOICES,
                               SPECIALTIES_CHOICES)
from django.contrib.auth.views import (LoginView, LogoutView, 
    PasswordResetView, PasswordResetDoneView,)
from django.contrib.auth import logout
from django.forms.models import model_to_dict
from apps.models import Plan, Member, UserToken
from normas.filters import PoliciesFilter
from normas.models import Areas_Normas, Policies_usage, Subtipo_Normas
from foro.models import Comentario_Foro
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery

# Johao #

from bus_normativa.models import date_normativa
from normas.models import Subcategories_Normas,Areas_Normas,Register_Normativa,Register_Palabraclave
from normas.serializer import normas_serializer, subtipos_uso_serializer, tipos_uso_serializer

from .utils import create_member_free, register_client_user
from .forms_register import MemberCapForm, ExternalUserForm

from membership.models import Membership
from apps.models import UsagePolicies, Order_payment, NiubizTransaction
from apps.niubiz import get_security_token, create_session_token, require_transaccion_autorizacion, create_niubiz_transaction, create_order_payment
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal


def busqueda_clavenormativa(request):
    area_normas=Areas_Normas.objects.all()

    item_area_normas=[]
    for i in area_normas:
        item_area_normas.append(
            {
                'id':i.id,
                'name':i.area_name
            }
        )
    context={
        'item_area_normas':item_area_normas,
        }
    return render(request,'normativa/normativa.html',context)

def busque_normativa(request):
    if request.method=='POST':
        pal_clave=request.POST['pal_clave'].upper()
        norma_tipo_uso=request.POST['tipo_uso'].upper()
        area_normas=Areas_Normas.objects.order_by('area_name')
        normas= None
        #normas = Register_Normativa.objects.filter(keywords__name__search=pal_clave).order_by('tipo_norma__order')
        
        # normas = Register_Normativa.objects.annotate(
        #                         search = SearchVector('keywords__name', 'norma','name_denom',
        #                          'base_legal')
        #                         ).filter(search=pal_clave).order_by('tipo_norma__order')

        if norma_tipo_uso == 'TODO':
            normas = Register_Normativa.objects.annotate(
                                search = SearchVector('keywords__name', 'norma','name_denom',
                                 'base_legal', config='Spanish')
                                ).filter(search=SearchQuery( pal_clave, config='Spanish')).order_by('tipo_norma__order')

        else:
            normas = Register_Normativa.objects.filter(
                    tipo_uso__area_name=norma_tipo_uso
                    ).annotate(search = SearchVector('keywords__name', 'norma','name_denom',
                                 'base_legal', config='Spanish')
                                ).filter(search=SearchQuery( pal_clave, config='Spanish')).order_by('tipo_norma__order')
        print(norma_tipo_uso)

        # print('#####===============')
        # for n in normas.values():
        #     print(n)
        #     print("--------------------------")
        #     print("SEARCH: ", n['search'])
        #     print('*********************')

        normas_results = []
        for n in normas:
            row ={
                'tipo_norma': n.tipo_norma.subcategory_name,
                'norma': n.norma,
                'name_denom': n.name_denom,
                'base_legal': n.base_legal,
                'document': n.document,
                'fecha_publi': n.fecha_publi,
                'tipo_uso' : n.tipo_uso
            }
            normas_results.append(row)

        context={ 
            'pal_clave'  : pal_clave,
            'area_normas':area_normas,
            'normas_results' : normas_results
        }

        return render(request,'normativa/normativa_busqueda.html',context)

    if request.method == 'GET':
        return render(request, 'normativa/normativa_busqueda.html')

# CRUD Palabra clave
def palabra_clave(request,codigo):
    normativa=Register_Normativa.objects.get(pk=codigo)
    # date_palaclave=Register_Palabraclave.objects.filter(normativa=codigo)
    palabras_claves_normativa = normativa.keywords.all()
    palabras_clave = Register_Palabraclave.objects.all()
    context={
        'normativa':normativa,
        # 'date_palaclave':date_palaclave
        'palabras_clave' : palabras_clave,
        'palabras_claves_normativa' : palabras_claves_normativa
        }
    return render(request,'norm_palabraclave/agregar_palabraclave.html',context)

def register_palabra_clave(request,codigo):
    normativa=Register_Normativa.objects.get(pk=codigo)
    palabra_clave=request.POST['palabra_clave']
    palabra_clave=palabra_clave.upper()
    Register_Palabraclave.objects.create(name=palabra_clave,normativa=normativa)
    date_palaclave=Register_Palabraclave.objects.filter(normativa=codigo)
    for a in date_palaclave:
        print(a.name)
    context={
       'normativa':normativa,
       'date_palaclave':date_palaclave
    }
    return render(request,'norm_palabraclave/datos_palabras_claves.html',context)

def delete_palclave(request, codigo):
    Register_Palabraclave.objects.filter(id=codigo).delete()
    return redirect('dateregister_norm')

def update_template(request,codigo):
    clave =Register_Palabraclave.objects.filter(id=codigo)
    context = {
        'clave':clave
    }
    return render(request,'norm_palabraclave/update_template_palclave.html',context)

def update_clave(request,codigo):
    if request.method=='POST':
        pala_clave=request.POST['pala_clave']
        pala_clave=pala_clave.upper()
        Register_Palabraclave.objects.filter(id=codigo).update(name=pala_clave)
        return redirect('dateregister_norm')

@login_required
def norma_edificatoria(request):
    return render(request,'normativa/normatividad_edificatoria.html',None)

@login_required
def norma_datos(request):
    norma_date = Register_Normativa.objects.order_by('tipo_norma').order_by('subtipo_uso.tipo_uso').order_by('subtipo_uso').order_by('norma')
    subcategories_normas = Subcategories_Normas.objects.order_by('order')
    area_normas = Areas_Normas.objects.order_by('area_name')
    palabras_clave = Register_Palabraclave.objects.all()
    subtipo_usos = Subtipo_Normas.objects.order_by('order')

    normas = [ normas_serializer(norma) for norma in norma_date ]
    sbu = [ subtipos_uso_serializer(sbu) for sbu in subtipo_usos ]
    tu = [ tipos_uso_serializer(tu) for tu in area_normas ]


    context={
            'norma_date':norma_date,
            'subcategories_normas':subcategories_normas, 
            'area_normas' : area_normas, 
            'palabras_clave' : palabras_clave,
            'subtipo_usos' : subtipo_usos,
            'normas' : json.dumps(normas),
            'sbu' : json.dumps(sbu),
            'tu' : json.dumps(tu),
            }
    return render(request,'normativa/norma_urb_edit.html',context)

# FILTRAR NORMATIVAS DE EDIFICACIONES
def filter_normativa_edificatoria(request):
    subnormativas = request.GET.getlist('subnormativas[]')        
    normativas = Register_Normativa.objects.filter(tipo_norma_id__in = subnormativas)
    return HttpResponse(normativas)

def normas_tecnicauso(request):
    return render(request,'normativa/norma_tecnuso.html',None)
def busqueda_provedor(request):
    return render(request,'proveedor/proveedor.html')
    
def busq_palclave_prov(request):
    if request.method=="POST":
        proveedor=[
            {'id':1,'palabra':'escalera','codigo':72154126,'name':'ADECCO CONSULTING S.A.'},
            {'id':2,'palabra':'escalera','codigo':72154127,'name':'AMERICATEL PERU S.A.'},
            {'id':3,'palabra':'escalera','codigo':72154128,'name':'ASE SYSTEM S.A.C'},
            {'id':4,'palabra':'ascensor','codigo':72154129,'name':'ASESORÍA SERVICIOS Y TECNOLOGÍA EN COMPUTO S.A.C'}
        ]

        name=request.POST['pal_clave']
        item_list=[]
        for _prov in proveedor:
            if _prov['palabra']==name:
                item_list.append(
                    {
                        'id':_prov['id'],
                        'palabra':_prov['palabra'],
                        'codigo':_prov['codigo'],
                        'name':_prov['name']
                    }
                )
        print(item_list)
        context={
            'proveedor':item_list,
        }
        return render(request,'proveedor/busqueda_proveedor.html',context)
        
    



# end #





# def get_rules(pk):
#     #rpta_normas = Master_Normas.objects.all()
#     rpta_normas = Master_Normas.objects.filter(area_name=pk)
#     rules = []
#     for i in rpta_normas:
#             rules.append(
#                 {
#                     'n': i.id,
#                     'section': i.category_name,
#                     'rule_type': i.subcategory_name,
#                     'locations': i.location_name,
#                     'norm': i.norma_rne,
#                     'denom': i.norma_name,
#                     'publication_date': i.validity_date_start,
#                     'file':i.file,
#                 }
#             )
#     return rules

        
def dashboard(request):
    return render(request, 'dashboard.html')

def get_user_by_form_data(data, roles=[]):
        user = {
        'names': data['names'],
        'first_surname': data['first_surname'],
        'second_surname': data['second_surname'],
        'profession': data['profession'],
        'tuition': data['tuition'],
        'is_signature_validated': False,
        'mobile': data['mobile'],
        'email': data['email'],
        'roles': roles
        }
        return user

class SignUpOthers(CreateView):

    model = Member
    form_class = ExternalRegisterForm
    template_name = 'sign-up.html'
    #success_url = reverse_lazy('profiles:check_your_email')

    def form_valid(self, form):
        print('INGRESO A VALIDO!')
        
        
        
        profile = form.save(commit=False)

        #group = Group.objects.get(name='Gratuito')      
        user = User.objects.create_user(profile.first_surname, profile.email, 'UEp8$x7rx@ZiSwU')
        #user = User.objects.create_user(profile.first_surname, profile.email, password)
        user.last_name = profile.first_surname
        #user.groups.add(group)
        user.save()


        #print('profile',profile)
        #registered_profile = Member.objects.filter(tuition=profile.tuition, profession=profile.profession)
        #if registered_profile:
        #    data = get_user_by_form_data(form.cleaned_data, ['PROP'])
        #    registered_profile.update(**data)
        token = UserToken(user_profile=profile)
        #else:
        profile.save()
        #profile.add_role(['PROP'])
        #profile.save()
            #token = UserToken(user_profile=profile)
        #token.save()
        #send_confirm_account(self.request, token.get_confirm_link(), profile.email)
        send_confirm_account(self.request, token.get_confirm_link(), profile.email)
        #return HttpResponseRedirect(reverse_lazy('profiles:check_your_email'))
        #return  reverse_lazy('dashboard:users')
        return HttpResponseRedirect(reverse_lazy('success_sign_up'))

    def form_invalid(self, form):
        print('INGRESO A INNVALIDO!',self,form)
        messages.error(self.request, 'Por favor, corrija los errores')
        return super(SignUpOthers, self).form_invalid(form)

class SignUpFormView(FormView):
    form_class = ExternalRegisterForm
    template_name = 'register/sign-up-user.html'
    success_url = reverse_lazy('success_sign_up')

    def form_valid(self, form):
        cd = form.cleaned_data
        print(cd)

        member = create_member_free(cd)
        password = cd['password']

        #group = Group.objects.get(name='Gratuito')      
        user = User.objects.create_user(member.tuition, member.email, password)
        user.last_name = member.first_surname
        #user.groups.add(group)
        user.save()
        #update member according to user created above
        m=Member.objects.get(id=member.id)
        m.user=user
        m.save()
        
        #token = UserToken(user_profile=member)
        #send_confirm_account(self.request, token.get_confirm_link(), member.email)

        return HttpResponseRedirect(reverse_lazy('success_sign_up'))

    # def form_invalid(self, form):
    #     print('INGRESO A INNVALIDO!',self,form)
    #     messages.error(self.request, 'Por favor, corrija los errores')
    #     return super(SignUpOthers, self).form_invalid(form)

class RegisterMemberTemplateView(TemplateView):
    """ Template View to sign up cap users  """

    template_name = 'register/sign-up-user.html'

    def get_context_data(self, **kwargs):
        exist_codigo_etica=UsagePolicies.objects.filter(title__icontains="codigo de etica").exists()

        context = super().get_context_data(**kwargs)
        context['formCap'] = MemberCapForm( prefix='formulario1')
        context['formExternal'] = ExternalUserForm( prefix='formulario2')
        context['pl_profesional'] = Membership.objects.get(membership_type="PLPP")
        context['pp_profesional'] = Membership.objects.get(membership_type="PPPP")
        if exist_codigo_etica:
            codigo_etica=UsagePolicies.objects.get(title__icontains="codigo de etica")
            context['codigo_etica'] = codigo_etica

        return context

def logout_view(request):
    logout(request)
    return redirect('login')


def users_register_erp(request):
    print('usuario: ',request.POST)
    if request.method == 'POST':
        print('usuario: ',request.POST)
    return render(request, 'register/user_register_erp.html')

def success_sign_up(request):
    messages.success(request, 'Registro Exitoso')
    return render(request, 'register/success_sign_up.html')	

def signup(request):
    return render(request, 'sign-up.html')

class Login(LoginView):
    authentication_form = UserLoginForm
    template_name = 'login/login-interactivo.html'

#####
#### start Payment process clients external PROFESIONAL PLAN list form
######         
class SignUpClients(FormView):
    template_name = 'checkout/profesional/register_form_cliente.html'
    form_class = ExternalUserForm
    success_url = reverse_lazy('client_choose_plan')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exist_codigo_etica=UsagePolicies.objects.filter(title__icontains="codigo de etica").exists()
        if exist_codigo_etica:
            codigo_etica=UsagePolicies.objects.get(title__icontains="codigo de etica")
            context['codigo_etica'] = codigo_etica

        return context

    def form_valid(self, form):
        cd = form.cleaned_data
        print(cd)
        member = register_client_user(cd)
        self.request.session['user_identity']= cd['identity']
        
        token = UserToken(user_profile=member)
        send_confirm_account(self.request, token.get_confirm_link(), member.email)

        return HttpResponseRedirect(reverse_lazy('client_choose_plan'))


def client_choose_plan(request):
    context={
        'pl_profesional': Membership.objects.get(membership_type="PLPP"),
    }
    return render(request, 'checkout/profesional/client_choose_plan.html', context)

def add_plan_client(request):
    if request.method == 'POST':
        cd = request.POST
        #SAVE THE PRICE IN THE SESSION
        r = request.session
        r['plan_price_client']= cd['plan_price_client']
    return redirect('checkout_client')

@csrf_exempt
def checkoutClient(request):
    COMERCIAL_ID = settings.COMERCIAL_ID
    type_membership = None
    plpp=Membership.objects.get(membership_type="PLPP")
    #price =  22.00
    price =  request.session.get('plan_price_client')
    try:
        member = Member.objects.get(identity=request.session.get('user_identity'))
    except:
        member=request.user.user_membership

    if plpp.price_month == Decimal(price):
        type_membership = "Plan mensual"
    if plpp.price_year == Decimal(price):
        type_membership= "Plan anual"
    purchase_number = 2022 #numero de pedido
    #purchase_number = request.user.username #numero de pedido
    security_token = get_security_token()
    token_session = create_session_token(security_token, price)
    context = {
        'pl_profesional': Membership.objects.get(membership_type="PLPP"),
        'token_security' : security_token,
        'token_session' : token_session,
        'comercial_id' : COMERCIAL_ID,
        'purchase_number': purchase_number,
        'price' : price,
        'type_membership':type_membership
        }

    if request.method == 'POST':
        cd = request.POST
        email=request.POST['customerEmail']
        token_transaccion = request.POST['transactionToken']
        #user=request.user.user_membership
        user=member
        print('checkout',cd)
        if request.POST['channel'] == 'pagoefectivo':
            url=request.POST['url']
            return redirect('client_cash_payment')

        transaction_success=require_transaccion_autorizacion(security_token, token_transaccion, price, purchase_number)
        print("transacion exitosa", transaction_success)
        niubiz_id = transaction_success['ecoreTransactionUUID']
        orden = create_order_payment(user,email,niubiz_id, price, type_membership)
        #create transaction niubiz
        create_niubiz_transaction(transaction_success, orden)
        #DELETE THE SESSION
        

        return redirect('success_payment_client')

    return render(request, 'checkout/profesional/checkout-client.html', context)

@csrf_exempt
def success_payment_client(request):
    try:
        order = Order_payment.objects.filter(identity=request.session.get('user_identity')).first()
        order = Order_payment.objects.filter(identity=request.user.user_membership.identity).first()
    except:
        pass
    
    context = {
        'order': order,
    }
    #del request.session['plan_price_client']
    #del request.session['user_identity']
    #request.session.modified = True
    return render(request, 'checkout/profesional/success_payment_cliente.html', context)

def client_cash_payment(request):
    return render(request, 'checkout/profesional/pago-efectivo-client.html')

#####
#### END Payment process clients external PROFESIONAL PLAN list form
######    


######################
#### START Payment process PLAN PREMIUM CAP
################
class SignUpPremiumCAP(FormView):
    template_name = 'checkout/premium_agremiado/register_form_premium_cap.html'
    form_class = ExternalUserForm
    success_url = reverse_lazy('checkout')

    def get_context_data(self):
        context = super().get_context_data()
        exist_codigo_etica=UsagePolicies.objects.filter(title__icontains="codigo de etica").exists()
        if exist_codigo_etica:
            codigo_etica=UsagePolicies.objects.get(title__icontains="codigo de etica")
            context['codigo_etica'] = codigo_etica

        return context

    def form_valid(self, form):
        cd = form.cleaned_data
        print(cd)
    
        # member = create_member_free(cd)
        # password = cd['password']

        # user = User.objects.create_user(member.tuition, member.email, password)
        # user.last_name = member.first_surname
        # user.save()
        # #update member according to user created above
        # m=Member.objects.get(id=member.id)
        # m.user=user
        # m.save()
        
        #token = UserToken(user_profile=member)
        #send_confirm_account(self.request, token.get_confirm_link(), member.email)

        return HttpResponseRedirect(reverse_lazy('checkout'))

def checkout_premium_cap(request):
    context = {
        'pl_premium_agremiado': Membership.objects.get(membership_type="PLPPA"),
        'pl_profesional': Membership.objects.get(membership_type="PLPP"),
        }
    return render(request, 'checkout/premium_agremiado/checkout_premium_cap.html', context)

def success_payment_cap(request):
    return render(request, 'checkout/premium_agremiado/success_payment_cap.html')

######################
#### END Payment process PLAN PREMIUM CAP
################


#########
### start Payment process -  PLAN AGREMIADO TO PREMIUM
##########
def cap_choose_plan(request):
    context={
        'pl_premium_agremiado': Membership.objects.get(membership_type="PLPPA"),
    }
    return render(request, 'checkout/premium_free/cap_choose_plan.html', context)

def add_plan_cap(request):
    if request.method == 'POST':
        cd = request.POST
        #SAVE THE PRICE IN THE SESSION
        r = request.session
        r['plan_price']= cd['plan_price']
    return redirect('checkout_cap')

@csrf_exempt
def checkoutCAP(request):
    COMERCIAL_ID = settings.COMERCIAL_ID
    type_membership = None
    plppa=Membership.objects.get(membership_type="PLPPA")
    #price =  22.00
    price =  request.session.get('plan_price')
    if plppa.price_month == Decimal(price):
        type_membership = "Plan mensual"
    if plppa.price_year == Decimal(price):
        type_membership= "Plan anual"
    #purchase_number = 2022 #numero de pedido
    purchase_number = request.user.username #numero de pedido
    security_token = get_security_token()
    token_session = create_session_token(security_token, price)
    context = {
        'pl_premium_agremiado': Membership.objects.get(membership_type="PLPPA"),
        'token_security' : security_token,
        'token_session' : token_session,
        'comercial_id' : COMERCIAL_ID,
        'purchase_number': purchase_number,
        'price' : price,
        'type_membership':type_membership
        }

    if request.method == 'POST':
        cd = request.POST
        email=request.POST['customerEmail']
        token_transaccion = request.POST['transactionToken']
        user=request.user.user_membership
        print('checkout',cd)
        if request.POST['channel'] == 'pagoefectivo':
            url=request.POST['url']
            return redirect('cap_cash_payment')

        transaction_success=require_transaccion_autorizacion(security_token, token_transaccion, price, purchase_number)
        print("transacion exitosa", transaction_success)
        niubiz_id = transaction_success['ecoreTransactionUUID']
        orden = create_order_payment(user,email,niubiz_id, price, type_membership)
        #create transaction niubiz
        create_niubiz_transaction(transaction_success, orden)
        #DELETE THE SESSION
        del request.session['plan_price']
        request.session.modified = True

        return redirect('success_suscription_cap')

    return render(request, 'checkout/premium_free/checkoutCAP.html', context)

#@requires_csrf_token
@csrf_exempt
def success_suscription_cap(request):
    order = Order_payment.objects.filter(identity=request.user.user_membership.identity).first()
    context = {
        'order': order,
    }
    return render(request, 'checkout/premium_free/success-suscription.html', context)

def cap_cash_payment(request):
    print(request.GET)
    print(request.POST)
    return render(request, 'checkout/premium_free/success-pagoefectivo.html')

#########
### end Payment process -  PLAN AGREMIADO TO PREMIUM
##########

def history_purchase(request):
    user =  request.user.user_membership.identity
    orders = Order_payment.objects.filter(identity=user)
    context = {
        'orders': orders,
    }
    return render(request, 'checkout/premium_free/history_purchase.html' , context)



@login_required
def preguntas(request):
    tipo_uso = Areas_Normas.objects.order_by('area_name')
    page = request.GET.get('page', 1)

    queryset = Policies_usage.objects.all()
    filter = PoliciesFilter(request.GET, queryset=queryset)

    queryset = filter.qs
    paginator = Paginator(queryset, 2)
    queryset = paginator.page(page)

    context = {
                'entity': queryset,
                'tipo_uso' : tipo_uso,
                'filter' : filter,
                'paginator' : paginator,
                }

    return render(request, 'preguntas.html', context)

@login_required
def filter_preguntas(request):
    tipo_uso_id = request.GET.get('tipo_uso_id', 0)
    pregunta = request.GET.get('pregunta', '')
    
    preguntas = Policies_usage.objects.filter(title__icontains = pregunta)



def password_reset(request):
    #cuestions = Policies_usage.objects.all()
    #cuestions = Policies_usage.objects.filter(pk=2)
    #for staff in cuestions:
    #    print (staff.norma_name.all())     
    context = {'cuestions': ''}
    return render(request, 'password_reset.html', context)



def preguntas_edit(request, pk=None):
    
    if request.method == "POST":
       form = PlanForm(request.POST) # Bound form
       post = form.save(commit=False)
       post.id=pk
       post.save()
       messages.success(request, 'Registro Guardado..!!')
       return redirect('/plan')

    else: 
        print('GET')
        if pk:
            plans = Plan.objects.get(id=pk)  
            data=model_to_dict(plans)  
            context ={'form': PlanForm(initial=data)}
            return render(request, 'plan_edit.html', context)
        else:
            form = PlanForm()
            context ={'form': form}
            return render(request, 'plan_edit.html',context)

def preguntas_delete(request, pk):
    print ('entro a borrar')
    plans = Plan.objects.get(id=pk)
    plans.delete()
    return redirect('/plan')




def plan_list(request):
    
    context = {
        'pl_agremiado': Membership.objects.get(membership_type="PLPA"),
        'pl_premium_agremiado': Membership.objects.get(membership_type="PLPPA"),
        'pl_profesional': Membership.objects.get(membership_type="PLPP"),
        'pp_agremiado': Membership.objects.get(membership_type="PPPA"),
        'pp_premium_agremiado': Membership.objects.get(membership_type="PPPPA"),
        'pp_profesional': Membership.objects.get(membership_type="PPPP"),
        }
    return render(request, 'plan/plan_list.html', context)

def plan_external_user(request):
    context = {
        'pl_profesional': Membership.objects.get(membership_type="PLPP"),
        'pp_profesional': Membership.objects.get(membership_type="PPPP"),
        }
    return render(request, 'plan/plan_external_user.html', context)

def carga_rules(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'carga_rules.html', context)


def plan(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'plan.html', context)

#https://elbauldelprogramador.com/crear-formularios-en-django-partir-de-un-modelo-con-modelform/
def plan_edit(request, pk=None):
    
    if request.method == "POST":
       form = PlanForm(request.POST) # Bound form
       post = form.save(commit=False)
       post.id=pk
       post.save()
       messages.success(request, 'Registro Guardado..!!')
       return redirect('/plan')

    else: 
        print('GET')
        if pk:
            plans = Plan.objects.get(id=pk)  
            data=model_to_dict(plans)  
            context ={'form': PlanForm(initial=data)}
            return render(request, 'plan_edit.html', context)
        else:
            form = PlanForm()
            context ={'form': form}
            return render(request, 'plan_edit.html',context)



def plan_delete(request, pk):
    print ('entro a borrar')
    plans = Plan.objects.get(id=pk)
    plans.delete()
    return redirect('/plan')

#def login(request):
#    return render(request, 'login.html')

HOME_CHOICES = {
        'id': '1',
        'name': 'Lima',
        }


def home(request):
    context = {
        'HOME_CHOICES': HOME_CHOICES,
    }
    print 
    return render(request, 'home.html', context)

def dash(request):
    afiliados = Member.objects.count()
    context = {
        'dashboard': True,
        'afiliados': afiliados,
    }
    return render(request, 'dash.html', context)


def works(request):
    context = {
        'works': True,
            'nonav': True,
            'places': MUNI_CHOICES[8:14],
            'areas': AREAS_CHOICES,
            'puestos': PUESTOS_CHOICES,
            'specialties': SPECIALTIES_CHOICES,
            'works_list': works_list,
    }
    if request.method == 'POST':
        context['alert'] = 'Registros Filtrados'
    return render(request, 'works.html', context)


def foro_comentarios(request):
    f_id = request.GET.get('rule_id')
    print ('ingreso Grabar!!')
    if request.method == "POST":
        comentario = request.POST.get('comentario')
        print ('POSTBOTON',comentario)
        b = Comentario_Foro(themas=f_id,user=request.user, coments=comentario)
        print ('POSTBBB',b)
        b.save()
        

    #print("request",f_id)
    comentarios = Comentario_Foro.objects.filter(user=1 ,themas=f_id)
    number_coments = comentarios.count()
    
    context = {
            'foro': True,
                'ncomentarios': number_coments,
                'comentarios_list': comentarios,
                'themes': [],
        }

    return render(request, 'foro_comentarios.html', context)

# def comentarios_save(request, pk=None):
    
#     post = get_object_or_404(Comentario_Foro, pk=pk)
   
#     if request.method == "POST":
#         form = CommentForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
            
#             #post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentForm(instance=post)
    

def index(request):
    context = {
        'dashboard': True,
            'munis': MUNI_CHOICES[1:11],
            'provs': PROVINCE_CHOICES,
            'cantidades': [random.randrange(1, 10000) for i in range(100)],
    }
    return render(request, 'dashboard.html', context)


def charts(request):
    context = {
        'charts': True,
    }
    return render(request, 'charts.html', context)


def member(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'member.html', context)


def configs(request):
    context = {
            'config': True,
    }
    return render(request, 'config.html', context)


def liquid(request):
    context = {
            'liquid': True,
            'form': LiquidForm(),
            'formset': SessionFormset(prefix='sessions'),
    }
    return render(request, 'liquid.html', context)


def comision(request):
    context = {
            'comision': True,
            'form': ComisionForm(),
            'formset': ArquitectFormset(),
    }
    return render(request, 'comision.html', context)


def entrevistas(request):
    context = {
            'entrevistas': True,
            'form': EntrevistaForm(),
            'formset': EntrevistaFormset(),
    }
    return render(request, 'entrevistas.html', context)
