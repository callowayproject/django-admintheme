==================
Django Admin Theme
==================

Goal
====

To provide a CSS-only skin for the Django's Admin app. This would allow adjustments to standard templates to work without modification.


Use
===

#. Install the app with ``pip install django-admintheme``.

#. Add ``admintheme`` to the top of ``INSTALLED_APPS``::

       INSTALLED_APPS = (
           'admintheme',
           'django.contrib.admin',
           # ...
       )
