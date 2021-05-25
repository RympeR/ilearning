from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.settings import preferences_settings
from dynamic_preferences.types import BasePreferenceType

global_preferences = global_preferences_registry.manager()

class PreferenceMixin(BasePreferenceType):
    @classmethod
    def key(cls):
        return '{}{}{}'.format(cls.section.name,
                               preferences_settings.SECTION_KEY_SEPARATOR,
                               cls.name)

    @classmethod
    def value(cls):
        return global_preferences[cls.key()]

