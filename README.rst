==================
Django Admin Theme
==================

Django Admin Theme is a CSS-only skin for the Django's Admin app. This allows
projects that make customizations to the standard admin templates to work
without modification.

Use
===

#. Install the app with ``pip install django-admintheme``.

#. Add ``admintheme`` to the top of ``INSTALLED_APPS``::

       INSTALLED_APPS = (
           'admintheme',
           'django.contrib.admin',
           # ...
       )
