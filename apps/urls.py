from django.urls import path, re_path

from .views_ajax import get_dni, RegisterCapAPIView, APIMemberView, RegisterExternalUsersAPIView
from .views import RegisterMemberTemplateView
from .views_plans import checkout

urlpatterns = [
    #register member
    path('sign-up-user/', RegisterMemberTemplateView.as_view(),name='sign-up-user'),
    
    path('dni/', get_dni, name='dni'),
    path('checkout/', checkout, name='checkout'),

    #api views
    path('api/cap/', RegisterCapAPIView.as_view(), name='api-cap'),
    path('api/member-erp/', APIMemberView.as_view(), name='api-member-erp'),
    path('api/member-external/', RegisterExternalUsersAPIView.as_view(), name='api-member-external'),


]