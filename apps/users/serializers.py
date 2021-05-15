from rest_framework import serializers
from apps.utils.customFields import TimestampField
from .models import (
    User,
    Payment,
    Subscription,
)


class UserGetSerializer(serializers.ModelSerializer):

    # birth_date = TimestampField(required=False)
    name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    ages_range = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'name',
            'last_name',
            'user_type',
            'birth_date',
            'ages_range'
        )

    def get_ages_range(self, obj: User):
        if getattr(obj, "students_start_age") and getattr(obj, "students_end_age"):
            return str(obj.students_start_age) + ' ' + str(obj.students_end_age)


class UserPartialSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'username', 'password'


class PaymentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = 'amount'

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        attrs['user'] = user
        return attrs


class PaymentGetSerializer(serializers.ModelSerializer):

    user = UserGetSerializer()

    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        exclude = 'paid', 'finished'


class SubscriptionGetSerializer(serializers.ModelSerializer):

    user = UserGetSerializer()

    class Meta:
        model = Subscription
        exclude = ('user', )

    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        attrs['user'] = user
        return attrs
