import random
from django.shortcuts import render
from .models import Coments_foro, Themas_foro
from normas.models import Master_Normas, Areas_Normas, Register_Normativa

def foro(request):

    context = {
        'foro': True,
        'normas': Register_Normativa.objects.all(),
        'last_themes': Themas_foro.objects.order_by('-register_date_time')
    }
    return render(request, 'foro/foro.html', context)


def foro_temas(request):
    context = {
        'foro': True,
        'category_list': [],
        'themes': [],
    }
    return render(request, 'foro/foro_temas.html', context)


def foro_comentarios(request, norma_id):

    norma = Register_Normativa.objects.get(id = norma_id)
    # f_id = request.GET.get('rule_id')
    # print ('ingreso Grabar!!')
    # if request.method == "POST":
    #     comentario = request.POST.get('comentario')
    #     print ('POSTBOTON',comentario)
    #     b = Coments_foro(themas=f_id,user=request.user, coments=comentario)
    #     print ('POSTBBB',b)
    #     b.save()
        

    #print("request",f_id)
    
    # normas = Master_Normas.objects.filter(id=f_id)
    # comentarios = Coments_foro.objects.filter(user=1 ,themas=f_id)
    # number_coments = comentarios.count()
    
    #data=model_to_dict(normas)  
    # if not normas:
    #     context = {
    #         'foro': True,
    #             'denominacion':'',
    #             'ncomentarios': 0,
    #             'comentarios_list': [],
    #             'themes': [],
    #     }    
    # else:
    #     context = {
    #         'foro': True,
    #             'denominacion':normas,
    #             'ncomentarios': number_coments,
    #             'comentarios_list': comentarios,
    #             'themes': [],
    #     }

    context = {
        'norma' : norma
    }


    #comentarios_save(f_id)
    #context = {'data': normas}
    #print ('foro_datos',context)
    return render(request, 'foro/foro_comentarios.html', context)

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
    

def get_foro_items():
    rpta_areas = Register_Normativa.objects.all()

    return rpta_areas

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


def get_themes():
	users = (
		('ariel12',False),
		('max2020',True),
		('superarquitecto',True),
		('megaarquitecto',False),
		('maria2021',False),
		('juan_12',True),
		('jorge_3',True),
		('jaime23',True),
	)
	themes = []
	for x in range(1,15):
		themes.append(
			{
				'theme': random.choice(random.choice(random.choice(get_foro_items())['items'])['last_messages'])['message'],
				'user': random.choice(users),
				'date':'Hoy {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
			},
		)
	return themes

def get_coments():
	themes = []
	for x in range(1,15):
		themes.append(
			{
				'theme': '',
				'user': '',
				'comment': '',
				'date':'Hoy {}:{} {}'.format(random.randint(1,12), random.randint(10,59), random.choice(['a.m.','p.m.'])),						
			},
		)
	return themes