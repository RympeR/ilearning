from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.utils.default_responses import (
    api_not_implemented_501
)
from .models import (
    User,
    Payment,
    Subscription,
)
from .serializers import (
    UserGetSerializer,
    UserCreationSerializer,
    PaymentCreateSerializer,
    PaymentGetSerializer,
    SubscriptionCreateSerializer,
    SubscriptionGetSerializer,
    UserPartialSerializer,
)
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin


class UserCreateAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer


class UserRetrieveAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetSerializer

    def get_object(self):
        return self.request.user


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetSerializer

    def get_object(self):
        return self.request.user


class UserPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserPartialSerializer

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PaymentCreateAPI(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer


class PaymentRetrieveAPI(generics.RetrieveDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentGetSerializer


class SubscriptionCreateAPI(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionCreateSerializer


class SubscriptionRetrieveAPI(generics.RetrieveDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionGetSerializer


class ChangeSubscriptionPlan(APIView):

    def put(self, request, pk):
        return api_not_implemented_501(
            {"status": "Don't understand logic -> DUDE)"}
        )
