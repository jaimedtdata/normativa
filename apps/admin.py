from django.contrib import admin
from django.apps import apps
#from .models import (Location_Normas)
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
from normas.models import Register_Normativa,Register_Palabraclave, Policies_usage
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    # list_display= ['names', 'first_surname' ,'identity','tuition', 'email', 'is_enabled', 'has_tutition' ,'penalty_fee']
    list_display= ['names', 'first_surname' ,'identity','tuition', 'email']
admin.site.register(Member,MemberAdmin)


#johao
class Register_NormativaAdmin(admin.ModelAdmin):
    list_display=('id','norma','name_denom','base_legal','fecha_publi','tipo_norma','tipo_uso','document')
    #readonly_fields = ['created', 'updated']    
    list_filter = ['es_vigente', 'created', 'name_denom']

class Register_PalabraclaveAdmin(admin.ModelAdmin):
    list_display=('id','name','normativa')

class SubNormativaAdmin(admin.ModelAdmin):
    list_display=('norma','norma_sub')

admin.site.register(Register_Normativa,Register_NormativaAdmin)
admin.site.register(Register_Palabraclave)
admin.site.register(Policies_usage)
#
class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)

# # Register your models here.
# class Control_paymentAdmin(admin.ModelAdmin):
#     list_filter = ['id_plan']
#     search_fields = ['member']
#     list_display =['member','id_plan','pay_method','pay_import','validity_date_start','validity_date_finish']
# admin.site.register(Control_payment, Control_paymentAdmin)

models = apps.get_models()


for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        #if 'django.contrib.sessions.models.Session' == model:
        #print (model)
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.unregister(Session)
admin.site.unregister(ContentType)
admin.site.unregister(LogEntry)
#https://realpython.com/customize-django-admin-python/
# models = apps.get_models()

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass