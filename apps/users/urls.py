from django.urls import path
from .views import (
    UserCreateAPI,
    UserRetrieveAPI,
    UserUpdateAPI,
    UserDeleteAPI,
    UserPartialUpdateView,
    PaymentCreateAPI,
    PaymentRetrieveAPI,
    SubscriptionCreateAPI,
    SubscriptionRetrieveAPI,
    ChangeSubscriptionPlan,
)

urlpatterns = [
    path('create-profile/', UserCreateAPI.as_view(), name='create-profile',),
    path('get-profile/', UserRetrieveAPI.as_view(), name='get-profile',),
    path('update-profile/', UserUpdateAPI.as_view(), name='action-profile',),
    path('delete-profile/', UserDeleteAPI.as_view(), name='action-profile',),
    path('partial-update-profile/', UserPartialUpdateView.as_view(), name='partial-update-profile'),
    path('create-payment/', PaymentCreateAPI.as_view(), name='create-payment',),
    path('get-payment/<int:pk>', PaymentRetrieveAPI.as_view(), name='get-payment',),
    path('create-subscription/', SubscriptionCreateAPI.as_view(), name='create-subscription',),
    path('get-subscription/<int:pk>', SubscriptionRetrieveAPI.as_view(), name='get-subscription',),
    path('change-subscription-plan/<int:pk>', ChangeSubscriptionPlan.as_view(), name='change-subscription-plan'),
]
