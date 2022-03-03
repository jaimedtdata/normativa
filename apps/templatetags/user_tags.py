# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Stdlib imports

# Core Django imports
from django import template
from django.contrib.auth.models import Group 
# Third-party app imports

# Realative imports of the 'app-name' package


register = template.Library()


# @register.filter('has_group')
# def has_group(user, group_name):
#     """
#     Verifica se este usuário pertence a um grupo
#     """
#     groups = user.groups.all().values_list('name', flat=True)
#     return True if group_name in groups else False

# from django import template

# register = template.Library() 

# @register.filter(name='has_group') 
# def has_group(user, group_name):
#     return user.groups.filter(name=group_name).exists() 
# In your template:

# {% if request.user|has_group:"mygroup" %} 
#     <p>User belongs to my group 
# {% else %}
#     <p>User doesn't belong to mygroup</p>
# {% endif %}

@register.filter(name='has_group')
def has_group(user, group_name): 
    group = Group.objects.get(name=group_name) 
    return True if group in user.groups.all() else False



    