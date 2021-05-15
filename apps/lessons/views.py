from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.utils.default_responses import (
    api_not_implemented_501
)
from .models import (
    Card,
    PurchasedCard,
    Group,
    Plan,
    Collection,
    PlanCard,
)
from .serializers import (
    CardGetSerializer,
    PurchasedCardGetSerializer,
    PurchasedCardCreateSerializer,
    GroupGetSerializer,
    GroupCreateSerializer,
    PlanCardRetrieveSerializer,
    PlanCardCreateSerializer,
    PlanGetSerializer,
    PlanCreateSerializer,
    PlanCardGetSerializer,
    CollectionGetSerializer,
    CollectionCreateSerializer,
)
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin



class CardCreateListAPI(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Card.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CardGetSerializer

class CardRetrieveAPI(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Card.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CardGetSerializer

class CardFilteredAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, filters):
        return api_not_implemented_501(
            {"status": "i don't fucking wanna do custom filters"}
        )

    
class PurchasedCardCreateAPI(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = PurchasedCard.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PurchasedCardCreateSerializer
    
class PurchasedCardListAPI(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = PurchasedCard.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = PurchasedCardCreateSerializer


class CardRetrieveAPI(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Card.objects.all()
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    serializer_class = CardGetSerializer


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
