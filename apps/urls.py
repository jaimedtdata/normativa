from django.urls import path, re_path, include
from rest_framework import routers

from .views_ajax import get_dni, RegisterCapAPIView, APIMemberView, APiViewSetERP
from .views import ( RegisterMemberTemplateView, plan_list, plan_external_user, checkoutClient,
                         checkoutCAP, success_suscription_cap, SignUpClients, success_payment_client,
                         SignUpPremiumCAP, checkout_premium_cap, success_payment_cap, history_purchase,
                         cap_choose_plan, add_plan_cap, cap_cash_payment, add_plan_client, 
                         client_choose_plan, client_cash_payment, premium_choose_plan, add_plan_premium )

router = routers.DefaultRouter()
router.register(r'users-erp', APiViewSetERP, basename='usersErp')

urlpatterns = [
    #register member
    path('sign-up-user/', RegisterMemberTemplateView.as_view(),name='sign-up-user'),
    path('dni/', get_dni, name='dni'),
    path('plan_list/', plan_list, name='plan_list'),
    path('plan_external_user/', plan_external_user, name='plan_external_user'),
    #update agremiado to premium
    path('cap_choose_plan/', cap_choose_plan, name='cap_choose_plan'),
    path('add_plan_cap/', add_plan_cap, name='add_plan_cap'),
    path('checkout-cap/', checkoutCAP, name='checkout_cap'),
    path('success_suscription_cap/', success_suscription_cap, name='success_suscription_cap'),
    path('cap_cash_payment/', cap_cash_payment, name='cap_cash_payment'),
    
    # clients (PROFESIONAL PLAN)
    path('sign-up-clients/', SignUpClients.as_view(), name='sign-up-clients'),
    path('client_choose_plan/', client_choose_plan, name='client_choose_plan'),
    path('add-plan-client/', add_plan_client, name='add_plan_client'),
    path('checkout-client/', checkoutClient, name='checkout_client'),
    path('success-payment-client/', success_payment_client, name='success_payment_client'),
    path('client-cash-payment/', client_cash_payment, name='client_cash_payment'),
    # Premium agremiado
    path('signup-premium-cap/', SignUpPremiumCAP.as_view(), name='signup-premium-cap'),
    path('premium-choose-plan/', premium_choose_plan, name='premium_choose_plan'),
    path('add-plan-premium/', add_plan_premium, name='add_plan_premium'),
    path('checkout-premium-cap/', checkout_premium_cap, name='checkout-premium-cap'),
    path('success-payment-cap/', success_payment_cap, name='success_payment_cap'),
    path('history-purchase/', history_purchase, name='history_purchase'),

    #api views
    path('api/cap/', RegisterCapAPIView.as_view(), name='api-cap'),
    #path('api/member-external/', RegisterExternalUsersAPIView.as_view(), name='api-member-external'),
    path('api/member-erp/', APIMemberView.as_view(), name='api-member-erp'),
    path('api/', include(router.urls)),

]

