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
    CollectionGetSerializer,
    CollectionCreateSerializer,
    GroupPartialSerializer,
    PlanPartialSerializer,
    CollectionPartialSerializer,
)
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin


class CardListAPI(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Card.objects.all()
    serializer_class = CardGetSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CardRetrieveAPI(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Card.objects.all()
    serializer_class = CardGetSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CardFilteredAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def get(self, filters):
        return api_not_implemented_501(
            {"status": "i don't fucking wanna do custom filters"}
        )


class PurchasedCardCreateAPI(generics.CreateAPIView):
    queryset = PurchasedCard.objects.all()
    serializer_class = PurchasedCardCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class PurchasedCardListAPI(generics.ListAPIView):
    queryset = PurchasedCard.objects.all()
    serializer_class = PurchasedCardGetSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        return PurchasedCard.objects.filter(user=self.request.user)


class GroupListAPI(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupGetSerializer

    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)


class GroupGetAPI(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupGetSerializer


class GroupCreateAPI(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class GroupPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = Group.objects.all()
    serializer_class = GroupPartialSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_serializer_context(self):
        return {'request': self.request}


class GroupDestroyAPI(generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CollectionListAPI(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionGetSerializer

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)


class CollectionGetAPI(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = CollectionGetSerializer


class CollectionCreateAPI(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = CollectionCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class CollectionPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = Group.objects.all()
    serializer_class = CollectionPartialSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_serializer_context(self):
        return {'request': self.request}


class CollectionDestroyAPI(generics.DestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PlanListAPI(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanGetSerializer

    def get_queryset(self):
        return Plan.objects.filter(user=self.request.user)


class PlanGetAPI(generics.RetrieveAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanGetSerializer


class PlanCreateAPI(generics.CreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PlanDestroyAPI(generics.DestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanCreateSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class PlanPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = Plan.objects.all()
    serializer_class = PlanPartialSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def get_serializer_context(self):
        return {'request': self.request}


class PlanCardListAPI(generics.ListAPIView):
    queryset = PlanCard.objects.all()
    serializer_class = PlanCardRetrieveSerializer

    def get_queryset(self):
        return PlanCard.objects.filter(plan__user=self.request.user).order_by('order')


class PlanCardGetAPI(generics.RetrieveAPIView):
    queryset = PlanCard.objects.all()
    serializer_class = PlanCardRetrieveSerializer


class PlanCardCreateAPI(generics.CreateAPIView):
    queryset = PlanCard.objects.all()
    serializer_class = PlanCardCreateSerializer


class PlanCardDestroyAPI(generics.DestroyAPIView):
    queryset = PlanCard.objects.all()
    serializer_class = PlanCardCreateSerializer
