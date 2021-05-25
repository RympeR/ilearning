from dynamic_preferences.types import FloatPreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from apps.utils.utils import PreferenceMixin

subscription = Section('subscription')


@global_preferences_registry.register
class SubscriptionCommission(PreferenceMixin, FloatPreference):
    section = subscription
    name = 'comission_percent'
    help_text = 'Процент комиссии при переходе межджу планами подписки'
    default = 10.0

    def validate(self, value):
        if value < 0:
            raise ValueError('Комиссия не может быть отрицательной')
