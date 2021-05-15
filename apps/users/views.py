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
    UserCreateSerializer,
    PaymentCreateSerializer,
    PaymentGetSerializer,
    SubscriptionCreateSerializer,
    SubscriptionGetSerializer,
    UserPartialSerializer,
)
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin


class UserCreateAPI(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = UserCreateSerializer


class UserRetrieveAPI(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = UserGetSerializer

    def get_object(self):
        return self.request.user


class UserAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = UserGetSerializer

    def get_object(self):
        return self.request.user


class UserPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserPartialSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class PaymentCreateAPI(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Payment.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PaymentCreateSerializer


class PaymentRetrieveAPI(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Payment.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PaymentGetSerializer


class SubscriptionCreateAPI(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Subscription.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = SubscriptionCreateSerializer


class SubscriptionRetrieveAPI(generics.RetrieveDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Subscription.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = SubscriptionGetSerializer

class ChangeSubscriptionPlan(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    parser_classes = (JSONParser, MultiPartParser, FormParser)

    def put(self, request, pk):
        return api_not_implemented_501(
            {"status": "Don't understand logic -> DUDE)"}
        )
