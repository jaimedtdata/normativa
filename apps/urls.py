from django.urls import path, re_path

from .views_ajax import get_dni, RegisterCapAPIView, APIMemberView, RegisterExternalUsersAPIView
from .views import ( RegisterMemberTemplateView, plan_list, plan_external_user, checkout,
                         checkoutCAP, success_suscription_cap, SignUpClients, success_payment_client )

urlpatterns = [
    #register member
    path('sign-up-user/', RegisterMemberTemplateView.as_view(),name='sign-up-user'),
    path('dni/', get_dni, name='dni'),
    path('plan_list/', plan_list, name='plan_list'),
    path('plan_external_user/', plan_external_user, name='plan_external_user'),
    path('checkout/', checkout, name='checkout'),
    path('checkout-cap/', checkoutCAP, name='checkout_cap'),
    path('success_suscription_cap/', success_suscription_cap, name='success_suscription_cap'),
    path('sign-up-clients/', SignUpClients.as_view(), name='sign-up-clients'),
    path('success-payment-client/', success_payment_client, name='success_payment_client'),



    #api views
    path('api/cap/', RegisterCapAPIView.as_view(), name='api-cap'),
    path('api/member-erp/', APIMemberView.as_view(), name='api-member-erp'),
    path('api/member-external/', RegisterExternalUsersAPIView.as_view(), name='api-member-external'),


]