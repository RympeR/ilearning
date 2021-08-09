from rest_framework import serializers
from apps.info.serializers import (
    TaskTypesGetSerializer,
    LearningRangeGetSerializer,
    LearningSubjectsGetSerializer,
    LessonThemeGetSerializer,
    LessonTypesGetSerializer,
    EducationProcessesGetSerializer,
    AttachmentGetSerializer,
)
from apps.users.serializers import (
    UserGetSerializer
)
from apps.users.models import (
    User,
    Subscription,
)
from .models import (
    Card,
    PurchasedCard,
    Group,
    Plan,
    Collection,
    PlanCard,
)
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone
from datetime import datetime, timedelta


class CardGetSerializer(serializers.ModelSerializer):

    card_type = TaskTypesGetSerializer()
    learning_range = LearningRangeGetSerializer(required=False, many=True)
    learning_subjects = LearningSubjectsGetSerializer(
        required=False, many=True)
    learning_themes = LessonThemeGetSerializer(required=False, many=True)
    learning_types = LessonTypesGetSerializer(required=False, many=True)
    education_process = EducationProcessesGetSerializer(
        required=False, many=True)
    images = AttachmentGetSerializer(required=False, many=True)
    bought = serializers.SerializerMethodField(required=False)
    favourite = serializers.SerializerMethodField(required=False)
    hosting_url = serializers.URLField(required=False)

    class Meta:
        model = Card
        fields = '__all__'

    def get_favourite(self, card: Card):
        request = self.context.get('request')
        user = None
        if request.user:
            user = request.user
            if user in card.favourites.all():
                return True
        return False

    def get_bought(self, card: Card):
        request = self.context.get('request')
        user = None
        if request.user:
            user = request.user
        if user:
            if card.accessory_level == 1:
                purchased_card = PurchasedCard.objects.filter(
                    user=user,
                    card=card
                )
                if purchased_card.exists():
                    return True


            elif card.accessory_level == 2:
                subs = Subscription.objects.filter(
                    user=user,
                    end_date__gte=(timezone.now())
                )
                if subs.exists():
                    return True
                return False
        return False

    def get_preview(self, attachemnt):
        request = self.context.get('request')
        if attachemnt.preview and getattr(attachemnt.preview, 'url'):
            file_url = attachemnt.preview.url
            return request.build_absolute_uri(file_url)
        return None

    def get_attachment(self, attachemnt):
        request = self.context.get('request')
        if attachemnt.attachemnt and getattr(attachemnt.attachemnt, 'url'):
            file_url = attachemnt.attachment.url
            return request.build_absolute_uri(file_url)
        return None

    def get_video(self, attachemnt):
        request = self.context.get('request')
        if attachemnt.video and getattr(attachemnt.video, 'url'):
            file_url = attachemnt.video.url
            return request.build_absolute_uri(file_url)
        return None


class PurchasedCardGetSerializer(serializers.ModelSerializer):

    user = UserGetSerializer()
    card = CardGetSerializer()

    class Meta:
        model = PurchasedCard
        fields = '__all__'


class PurchasedCardCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchasedCard
        exclude = ('user', )

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        attrs['user'] = user
        return attrs


class GroupGetSerializer(serializers.ModelSerializer):

    user = UserGetSerializer()

    class Meta:
        model = Group
        fields = '__all__'


class GroupCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        attrs['user'] = user
        return attrs


class GroupPartialSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False)
    duration = serializers.CharField(required=False)
    age = serializers.CharField(required=False)

    class Meta:
        model = Group
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        attrs['user'] = user
        return attrs

##


class PlanCardRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanCard
        fields = '__all__'


class PlanCardCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanCard
        fields = '__all__'

##


class PlanGetSerializer(serializers.ModelSerializer):

    user = UserGetSerializer()
    cards = CardGetSerializer(many=True)
    groups = GroupGetSerializer(many=True)
    case_to_cards = PlanCardRetrieveSerializer(many=True)

    class Meta:
        model = Plan
        fields = (
            'pk',
            'name',
            'user',
            'cards',
            'case_to_cards',
            'groups'
        )


class PlanCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        attrs['user'] = user
        return attrs


class PlanPartialSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    user = serializers.PrimaryKeyRelatedField(
        required=False, queryset=User.objects.all())
    cards = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Card.objects.all(), many=True)
    groups = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Group.objects.all(), many=True)

    class Meta:
        model = Plan
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        attrs['user'] = user
        return attrs
##


class PlanCardGetSerializer(serializers.ModelSerializer):

    plan = PlanGetSerializer()
    card = CardGetSerializer()

    class Meta:
        model = PlanCard
        fields = '__all__'
##


class CollectionGetSerializer(serializers.ModelSerializer):

    user = UserGetSerializer()
    cards = CardGetSerializer(many=True)

    class Meta:
        model = Collection
        fields = '__all__'


class CollectionCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        required=True, queryset=User.objects.all())
    cards = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Card.objects.all(), many=True)
    class Meta:
        model = Collection
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        attrs['user'] = user
        return attrs


class CollectionPartialSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    user = serializers.PrimaryKeyRelatedField(
        required=False, queryset=User.objects.all())
    cards = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Card.objects.all(), many=True)

    class Meta:
        model = Collection
        fields = '__all__'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        attrs['user'] = user
        return attrs
