from rest_framework import serializers

class TimestampField(serializers.Field):
    def to_representation(self, value):
        return value.timestamp()

    def to_internal_value(self, value):
        return value

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
