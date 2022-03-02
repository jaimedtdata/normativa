import json
import uuid
import random
from datetime import datetime
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

from apps.email import (send_confirm_account, send_success_sign_up,
    send_password_reset, send_success_password_reset,)

from django.views.generic import CreateView, FormView
from django.urls import reverse, reverse_lazy
from apps.forms import ( SignUpForm ,LiquidForm, SessionFormset, ComisionForm,PlanForm,
                CommentForm,  ArquitectFormset, EntrevistaFormset, EntrevistaForm, MUNI_CHOICES,
                PROVINCE_CHOICES, RulesForm, UserLoginForm, ExternalRegisterForm)
from apps.choices import (AREAS_CHOICES, PUESTOS_CHOICES,
                               works_list, get_themes, SANCTIONS_CATEGORIES, PREVENTIONS_CHOICES,
                               SPECIALTIES_CHOICES)
from django.contrib.auth.views import (LoginView, LogoutView, 
    PasswordResetView, PasswordResetDoneView,)
from django.forms.models import model_to_dict
from apps.models import Plan, Policies_usage, Member, UserToken
from normas.models import Areas_Normas,Master_Normas,Categories_Normas
from foro.models import Coments_foro
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery

# Johao #

from bus_normativa.models import date_normativa
from normas.models import Subcategories_Normas,Areas_Normas,Register_Normativa,Register_Palabraclave,SubNormativa
from normas.serializer import normas_serializer


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
        area_normas=Areas_Normas.objects.all()
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

# CRUD Normativa
def tipo_normativa(request):
   normativa = Subcategories_Normas.objects.order_by('order')
   tipo_uso=Areas_Normas.objects.all()
   palabras_clave = Register_Palabraclave.objects.all()
   context = {
        'normativa':normativa,
        'tipo_uso':tipo_uso,
        'palabras_clave' : palabras_clave,
        'fecha_hoy' : datetime.today().strftime('%Y-%m-%d')
    }
   return render(request,'normativa/form_normativa.html',context)

def register_normativa(request):
    if request.method=='POST':
        norma=request.POST['norma']
        name_deno=request.POST['name_deno']
        base_legal=request.POST['base_legal']
        fecha_publi=request.POST['fecha_publi']
        tip_norma=request.POST['tip_norma']
        tip_uso=request.POST['tip_uso']
        file_pdf= request.FILES.get('documento', None)
        es_foro = True if request.POST.get('es_foro', False) == 'on' else False
        es_vigente = True if request.POST.get('es_vigente', False) == 'on' else False
        descripcion = request.POST['descripcion']
        pcs = request.POST.getlist('palabras_clave[]')

        normativa = Register_Normativa.objects.create(norma=norma,name_denom=name_deno,base_legal=base_legal,
                    fecha_publi=fecha_publi,tipo_norma_id=tip_norma,tipo_uso_id=tip_uso,document=file_pdf,es_foro=es_foro, es_vigente=es_vigente, descripcion=descripcion)

        # AQUI AGREGO, TAL VEZ SE PUEDA USAR OTRO METODO IDK
        for pc in pcs:
            objx, created = Register_Palabraclave.objects.get_or_create(name = pc)
            objx.normativas.add(normativa)

        return redirect('dateregister_norm')

def date_register(request):
    norma_register = Register_Normativa.objects.order_by('norma')
    context = {
        'norma_register':norma_register
    }
    return render(request,'normativa/datenorma_register.html',context)

def edit_normativa(request,codigo):
    normativa=Register_Normativa.objects.get(pk=codigo)
    tipo_uso=Areas_Normas.objects.all()
    tipo_normativa=Subcategories_Normas.objects.order_by('order')
    palabras_clave = Register_Palabraclave.objects.all()
    palabras_claves_normativa = normativa.keywords.all()


    context = {
        'normativa':normativa,
        'tipo_uso':tipo_uso,
        'tipo_normativa':tipo_normativa,
        'palabras_clave' : palabras_clave,
        'palabras_claves_normativa' : palabras_claves_normativa,
        'fecha_hoy' : datetime.today().strftime('%Y-%m-%d')

    }

    return render(request,'normativa/edit_normativa.html',context)

def updatedate_normativa(request,codigo):
    if request.method=='POST':
        norma=request.POST['norma']
        name_deno=request.POST['name_deno']
        base_legal=request.POST['base_legal']
        fecha_publi=request.POST['fecha_publi']
        tip_norma=request.POST['tip_norma']
        tip_uso=request.POST['tip_uso']
        es_foro = True if request.POST.get('es_foro', False) == 'on' else False
        es_vigente = True if request.POST.get('es_vigente', False) == 'on' else False
        descripcion = request.POST['descripcion']

        
        file_pdf = request.FILES.get('documento', None)

        if file_pdf != None:
            fs = FileSystemStorage()
            Register_Normativa.objects.get(id=codigo).document.delete()
            filename = fs.save('Document_normativa/' + file_pdf.name, file_pdf)
            file_pdf = filename

        Register_Normativa.objects.filter(id=codigo).update(norma=norma,name_denom=name_deno,base_legal=base_legal,
        fecha_publi=fecha_publi,tipo_norma_id=tip_norma,tipo_uso_id=tip_uso,document=file_pdf,es_foro=es_foro, es_vigente=es_vigente, descripcion=descripcion)

        return redirect('dateregister_norm')

def delete_normativa(request,codigo):
    Register_Normativa.objects.filter(id=codigo).delete()
    return redirect('dateregister_norm')

#end  Normativa

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
        #return redirect('form_normativas')
# end Registrando Palabra clave
#
def norma_edificatoria(request):
    return render(request,'normativa/normatividad_edificatoria.html',None)
    
def norma_datos(request):
    norma_date = Register_Normativa.objects.order_by('norma')
    subtipo_normas = Subcategories_Normas.objects.order_by('order')
    area_normas = Areas_Normas.objects.all()
    palabras_clave = Register_Palabraclave.objects.all()

    normas = [ normas_serializer(norma) for norma in norma_date ]

    context={'norma_date':norma_date, 'subtipo_normas':subtipo_normas, 'normas' : json.dumps(normas), 'area_normas' : area_normas, 'palabras_clave' : palabras_clave}
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





def get_rules(pk):
    #rpta_normas = Master_Normas.objects.all()
    rpta_normas = Master_Normas.objects.filter(area_name=pk)
    rules = []
    for i in rpta_normas:
            rules.append(
                {
                    'n': i.id,
                    'section': i.category_name,
                    'rule_type': i.subcategory_name,
                    'locations': i.location_name,
                    'norm': i.norma_rne,
                    'denom': i.norma_name,
                    'publication_date': i.validity_date_start,
                    'file':i.file,
                }
            )
    return rules

        
def dashboard(request):
    rpta_areas = Areas_Normas.objects.all()
    context = {'rpta_areas': rpta_areas}
    print (context)
    return render(request, 'dashboard.html', context)


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

        group = Group.objects.get(name='Gratuito')      
        user = User.objects.create_user(profile.first_surname, profile.email, 'UEp8$x7rx@ZiSwU')
        #user = User.objects.create_user(profile.first_surname, profile.email, password)
        user.last_name = profile.first_surname
        user.groups.add(group)
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
        
        member, created = Member.objects.get_or_create(
                        names= cd['names'],
                        first_surname= cd['first_surname'], 
                        second_surname= cd['second_surname'], 
                        identity= cd['identity'], 
                        person_type= cd['person_type'], 
                        mobile= cd['mobile'], 
                        phone= cd['phone'], 
                        email= cd['email'], 
                        address= cd['address'], 
                        profession= cd['profession'], 
                        tuition= cd['tuition'], 
                        secret_code= cd['secret_code']
    )
        password = cd['password']

        group = Group.objects.get(name='Gratuito')      
        user = User.objects.create_user(member.tuition, member.email, password)
        user.last_name = member.first_surname
        user.groups.add(group)
        user.save()
        token = UserToken(user_profile=member)

        send_confirm_account(self.request, token.get_confirm_link(), member.email)

        return HttpResponseRedirect(reverse_lazy('success_sign_up'))

    # def form_invalid(self, form):
    #     print('INGRESO A INNVALIDO!',self,form)
    #     messages.error(self.request, 'Por favor, corrija los errores')
    #     return super(SignUpOthers, self).form_invalid(form)

def success_sign_up(request):
    messages.success(request, 'Registro Exitoso')
    return render(request, 'register/success_sign_up.html')	

def signup(request):
    return render(request, 'sign-up.html')

class Login(LoginView):
    authentication_form = UserLoginForm
    template_name = 'login/login-interactivo.html'

class LoginNuevo(LoginView):
    authentication_form = UserLoginForm
    template_name = 'login/login-interactivo.html'

#@login_required
def preguntas(request):

    norma_id = request.GET.get('norma_id')

    if norma_id == None:
        preguntas = Policies_usage.objects.all()
    else:
        preguntas = get_object_or_404(Register_Normativa, id = norma_id).preguntas_frecuentes.all()

    context = {'preguntas': preguntas}

    return render(request, 'preguntas.html', context)
    

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

def checkout(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'checkout.html', context)

def plan_list(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'plan_list.html', context)

def plan_list_login(request):
    plans = Plan.objects.all()
    context = {'plans': plans}
    return render(request, 'login/plan_list_login.html', context)

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
    context = {
        'dashboard': True,
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

@login_required
def rules(request):
   
    tipouso_id = request.GET.get('rule_id')
    print("request",tipouso_id)

    context = {
        'rules': True,
            'nonav': False,
            'categories': 'RULES_CATEGORIES',
            'sanctions': SANCTIONS_CATEGORIES,
            'preventions': PREVENTIONS_CHOICES,
            'filter': RulesForm(),
            'rules_list': get_rules(tipouso_id),
    }
    if request.method == 'POST':
        context['alert'] = 'Registros Filtrados'
    return render(request, 'rules.html', context)


def foro(request):
    context = {
        'foro': True,
            'category_list': get_foro_items(),
            'themes': get_themes(),
    }
    return render(request, 'foro.html', context)


def foro_temas(request):
    context = {
        'foro': True,
            'category_list': [],
            'themes': [],
    }
    return render(request, 'foro_temas.html', context)


def foro_comentarios(request):
    f_id = request.GET.get('rule_id')
    print ('ingreso Grabar!!')
    if request.method == "POST":
        comentario = request.POST.get('comentario')
        print ('POSTBOTON',comentario)
        b = Coments_foro(themas=f_id,user=request.user, coments=comentario)
        print ('POSTBBB',b)
        b.save()
        

    #print("request",f_id)
    
    normas = Master_Normas.objects.filter(id=f_id)
    comentarios = Coments_foro.objects.filter(user=1 ,themas=f_id)
    number_coments = comentarios.count()
    
    #data=model_to_dict(normas)  
    if not normas:
        context = {
            'foro': True,
                'denominacion':'',
                'ncomentarios': 0,
                'comentarios_list': [],
                'themes': [],
        }    
    else:
        context = {
            'foro': True,
                'denominacion':normas,
                'ncomentarios': number_coments,
                'comentarios_list': comentarios,
                'themes': [],
        }


    #comentarios_save(f_id)
    #context = {'data': normas}
    #print ('foro_datos',context)
    return render(request, 'foro_comentarios.html', context)

# def comentarios_save(request, pk=None):
    
#     post = get_object_or_404(Coments_foro, pk=pk)
   
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


def get_foro_items():
    rpta_areas = Areas_Normas.objects.all()
    
    category_list = []
    title_list = {}
    detail_list = []
    item_list = []

    for a in rpta_areas:

        title_list['title']= a.area_name.title()
        
        rpta_normas = Master_Normas.objects.filter(area_name=a.id)
        nmessages=rpta_normas.count()
        for i in rpta_normas:
                
                item_list.append(
                        {
                        'title':i.norma_name.title(),
                        'themes_count': i.id,
                        'messages_count': nmessages,
                        'id': i.id,
                        },
                )
                
                dictionary_title_list= item_list.copy()
        title_list['items']=dictionary_title_list
        item_list = []
        print (dictionary_title_list)
        
        dictionary_copy = title_list.copy()
        
        detail_list.append(dictionary_copy)

    
    
    return detail_list

    # col_list = ['norma_name', 'id']
    # category_list.append(
    #     {
    #         'title': rpta_areas[1],
    #         'items': Master_Normas.objects.all().values_list(*col_list),
    #     },

    # )
    # category_list = (
    #     {
    #         'title': 'Temas Normativos',
    #         'items': [
    #             {
    #                 'title':'Licencias, Procedimientos Administrativos  para Licencias de Edificación',
    #                 'themes_count': random.randint(10,50),
    #                 'messages_count': random.randint(50,200),
    #             },
    #             {
    #                 'title':'Convenios',
    #                 'themes_count': random.randint(10,50),
    #                 'messages_count': random.randint(50,200),
    #                 'last_messages': (
    #                     {
    #                         'message':'Convenio Rimac Seguros',
    #                         'date':'Hoy {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
    #                     },
    #                     {
    #                         'message':'Convenio Clínica Ricardo Palma',
    #                         'date':'Ayer {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
    #                     },
    #                 )
    #             },				
    #         ],
    #     },
        
    # )
    # return category_list