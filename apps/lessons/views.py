from django_filters.rest_framework import filterset
from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from apps.info.models import (
    LearningSubjects,
    LessonTheme,
    LessonTypes,
    EducationProcesses,
)
from apps.info.serializers import (
    LearningSubjectsGetSerializer,
    LessonThemeGetSerializer,
    LessonTypesGetSerializer,
    EducationProcessesGetSerializer,
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


def filter_related_objects(queryset, name, value, model, serializer, related_category):
    lookup = '__'.join([name, 'in'])
    if value:
        subjects = model.objects.get(pk=value[0].pk)
        look_related = '__'.join([related_category, 'gte'])
        hole_tree = model.objects.filter(
            Q(tree_id=subjects.tree_id) &
            Q(**{look_related: getattr(subjects, related_category)}) &
            Q(display=True)
        )
        values = [serializer(
            instance=subj).data['id'] for subj in hole_tree]
    else:
        subjects = model.objects.filter(display=True)
        values = [serializer(
            instance=subj).data['id'] for subj in subjects]
    return queryset.filter(**{lookup: values}).distinct()


class CardFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    price = filters.NumberFilter(lookup_expr='lte')
    learning_subjects = filters.ModelMultipleChoiceFilter(
        lookup_expr='in',
        queryset=LearningSubjects.objects.all(),
        field_name='learning_subjects',
        method='filter_learning_subjects'
    )
    learning_themes = filters.ModelMultipleChoiceFilter(
        lookup_expr='in',
        queryset=LessonTheme.objects.all(),
        field_name='learning_themes',
        method='filter_learning_themes'
    )
    learning_types = filters.ModelMultipleChoiceFilter(
        lookup_expr='in',
        queryset=LessonTypes.objects.all(),
        field_name='learning_types',
        method='filter_learning_types'
    )
    education_process = filters.ModelMultipleChoiceFilter(
        lookup_expr='in',
        queryset=EducationProcesses.objects.all(),
        field_name='education_process',
        method='filter_education_process'
    )

    def filter_learning_subjects(self, queryset, name, value):
        return filter_related_objects(queryset, name, value, LearningSubjects, LearningSubjectsGetSerializer, 'Подкатегория предмета')

    def filter_learning_themes(self, queryset, name, value):
        return filter_related_objects(queryset, name, value, LessonTheme, LessonThemeGetSerializer, 'Подкатегория темы занятия')

    def filter_learning_types(self, queryset, name, value):
        return filter_related_objects(queryset, name, value, LessonTypes, LessonTypesGetSerializer, 'Подкатегория типа занятия')

    def filter_education_process(self, queryset, name, value):
        return filter_related_objects(queryset, name, value, EducationProcesses, EducationProcessesGetSerializer, 'Подкатегория образовательного процесса')

    class Meta:
        model = Card
        fields = (
            'name',
            'language',
            'price',
            'valute',
            'card_type',
            'card_type',
            'learning_range',
            'learning_subjects',
            'learning_themes',
            'learning_types',
            'education_process',
        )


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


class CardFilteredAPI(generics.ListAPIView):
    queryset = Card.objects.all()
    filterset_class = CardFilter
    serializer_class = CardGetSerializer


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
