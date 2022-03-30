from django.contrib import admin
from django.apps import apps
#from .models import (Location_Normas)
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
from normas.models import Areas_Normas, Register_Normativa,Register_Palabraclave, Policies_usage, Subtipo_Normas, Tipo_Normas
from .models import Member, UsagePolicies, Order_payment
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class MemberResource(resources.ModelResource):
    class Meta:
        model = Member

class MemberAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display= ['names', 'first_surname' ,'identity','tuition', 'email']
    search_fields = ['names', 'first_surname' ,'identity','tuition', 'email']
    resource_class = MemberResource
admin.site.register(Member,MemberAdmin)

class Order_paymentAdmin(admin.ModelAdmin):
    list_display= ['names', 'first_surname', 'second_surname' , 'email','identity','created' ,'validity_date_start', 'validity_date_finish']
    search_fields = ['names', 'first_surname', 'second_surname' , 'email', 'identity']
    readonly_fields = ['created', 'updated']
admin.site.register(Order_payment,Order_paymentAdmin)

'''
    Normas Admin Site
'''

class Register_NormativaResource(resources.ModelResource):
    class Meta:
        model = Register_Normativa

class Register_NormativaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','norma','name_denom','base_legal','fecha_publi','tipo_norma','document')
    #readonly_fields = ['created', 'updated']    
    list_filter = ['estado', 'created', 'name_denom']
    resource_class = Register_NormativaResource
admin.site.register(Register_Normativa,Register_NormativaAdmin)

class Tipo_Normas_Resource(resources.ModelResource):
    class Meta:
        model = Tipo_Normas

class Tipo_Normas_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','name', 'order', 'created')     
    list_filter = ['name', 'created']
    resource_class = Tipo_Normas_Resource
admin.site.register(Tipo_Normas, Tipo_Normas_Admin)

class Areas_Normas_Resource(resources.ModelResource):
    class Meta:
        model = Areas_Normas

class Areas_Normas_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','name', 'order', 'created')     
    list_filter = ['name', 'created']
    resource_class = Areas_Normas_Resource
admin.site.register(Areas_Normas, Areas_Normas_Admin)

class Subtipo_Normas_Resource(resources.ModelResource):
    class Meta:
        model = Subtipo_Normas

class Subtipo_Normas_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display=('id','name', 'tipo_uso', 'order', 'created')     
    list_filter = ['name', 'created']
    resource_class = Subtipo_Normas_Resource
admin.site.register(Subtipo_Normas, Subtipo_Normas_Admin)

class Register_PalabraclaveAdmin(admin.ModelAdmin):
    list_display=('id','name','normativa')

class SubNormativaAdmin(admin.ModelAdmin):
    list_display=('norma','norma_sub')

class UsagePoliciesAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']

admin.site.register(Register_Palabraclave)
admin.site.register(Policies_usage, )
admin.site.register(UsagePolicies,UsagePoliciesAdmin )

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