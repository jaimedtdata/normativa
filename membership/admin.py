from django.contrib import admin
from .models import Membership, MembershipBenefits, APIMember
# Register your models here.

# @admin.register(Membership)
# class MemberShipAdmin(admin.ModelAdmin):
#     list_display= ['membership_type', 'get_benefits']
  

# @admin.register(MembershipBenefits)
# class MemberBenefitsAdmin(admin.ModelAdmin):
#     list_display= ['name']


# @admin.register(APIMember)
# class APIMemberAdmin(admin.ModelAdmin):
#      list_display= ['name_user', 'cap_num', 'identity', 'is_enabled', 'penalty_fee', 'has_tutition']


# @admin.register(Subscription)
# class SuscriptionAdmin(admin.ModelAdmin):
#     list_display= ['user_membership', 'active']