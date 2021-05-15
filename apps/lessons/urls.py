from django.urls import path
from .views import (
    CardListAPI,
    CardRetrieveAPI,
    CardFilteredAPI,
    PurchasedCardCreateAPI,
    PurchasedCardListAPI,
    GroupListAPI,
    GroupGetAPI,
    GroupCreateAPI,
    GroupPartialUpdateView,
    GroupDestroyAPI,
    CollectionListAPI,
    CollectionGetAPI,
    CollectionCreateAPI,
    CollectionPartialUpdateView,
    CollectionDestroyAPI,
    PlanListAPI,
    PlanGetAPI,
    PlanCreateAPI,
    PlanDestroyAPI,
    PlanPartialUpdateView,
    PlanCardListAPI,
    PlanCardGetAPI,
    PlanCardCreateAPI,
    PlanCardDestroyAPI,
    PlanPartialUpdateView,
)

urlpatterns = [
    path('card-list/', CardListAPI.as_view(), name='card-list'),
    path('card-get/<int:pk>', CardRetrieveAPI.as_view(), name='card-get'),
    path('card-filtered/', CardFilteredAPI.as_view(), name='card-filtered'),
    path('purchase-card-create/', PurchasedCardCreateAPI.as_view(), name='purchase-card-create'),
    path('purchase-card-list/', PurchasedCardListAPI.as_view(), name='purchase-card-list'),
    path('group-list/', GroupListAPI.as_view(), name='group-list'),
    path('group-get/<int:pk>', GroupGetAPI.as_view(), name='group-get'),
    path('group-create/', GroupCreateAPI.as_view(), name='group-create'),
    path('group-partial-update/<int:pk>', GroupPartialUpdateView.as_view(), name='group-partial-update'),
    path('group-destroy/<int:pk>', GroupDestroyAPI.as_view(), name='group-destroy'),
    path('collection-list/', CollectionListAPI.as_view(), name='collection-list'),
    path('collection-get/<int:pk>', CollectionGetAPI.as_view(), name='collection-get'),
    path('collection-create/', CollectionCreateAPI.as_view(), name='collection-create'),
    path('collection-partial-update/<int:pk>', CollectionPartialUpdateView.as_view(), name='collection-partial-update'),
    path('collection-destroy/<int:pk>', CollectionDestroyAPI.as_view(), name='collection-destroy'),
    path('plan-list/', PlanListAPI.as_view(), name='plan-list'),
    path('plan-get/<int:pk>', PlanGetAPI.as_view(), name='plan-get'),
    path('plan-create/', PlanCreateAPI.as_view(), name='plan-create'),
    path('plan-destroy/<int:pk>', PlanDestroyAPI.as_view(), name='plan-destroy'),
    path('plan-partial-update/<int:pk>', PlanPartialUpdateView.as_view(), name='plan-partial-update'),
    path('plan-card-list/', PlanCardListAPI.as_view(), name='plan-card-list'),
    path('plan-card-get/<int:pk>', PlanCardGetAPI.as_view(), name='plan-card-get'),
    path('plan-card-create/', PlanCardCreateAPI.as_view(), name='plan-card-create'),
    path('plan-card-destroy/<int:pk>', PlanCardDestroyAPI.as_view(), name='plan-card-destroy'),
    path('plan-card-partial-update/<int:pk>', PlanPartialUpdateView.as_view(), name='plan-card-partial-update'),
]
