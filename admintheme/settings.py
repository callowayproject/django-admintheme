from django.conf import settings

DEFAULT_SETTINGS = {

}

USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'admintheme_SETTINGS'))

globals().update(USER_SETTINGS)