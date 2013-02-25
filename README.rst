==================
Django Admin Theme
==================

Django Admin Theme is a CSS-only skin for the Django's Admin app. This allows
projects that make customizations to the standard admin templates to work
without modification.

.. contents::
   :local:

Screen shots
============

.. image:: https://raw.github.com/callowayproject/django-admintheme/master/doc_src/screenshots/login.png

.. image:: https://raw.github.com/callowayproject/django-admintheme/master/doc_src/screenshots/dashboard.png

.. image:: https://raw.github.com/callowayproject/django-admintheme/master/doc_src/screenshots/changelist.png

.. image:: https://raw.github.com/callowayproject/django-admintheme/master/doc_src/screenshots/changeform_success.png

.. image:: https://raw.github.com/callowayproject/django-admintheme/master/doc_src/screenshots/changeform_error.png


Use
===

#. Install the app with ``pip install django-admintheme``.

#. Add ``admintheme`` to the top of ``INSTALLED_APPS``::

       INSTALLED_APPS = (
           'admintheme',
           'django.contrib.admin',
           # ...
       )

How to Contribute
=================

* **Submit bugs.**
   * Enter them at https://github.com/callowayproject/django-admintheme/issues.
   * Include a screen shot if possible
   * Include HTML if it isn't common or if it is necessary
* **Give Feedback.**
   * Enter feedback as a bug (see above).
   * We'll keep it open for some discussion, if necessary, depending on other feedback.
* **Submit Patches.**
   * Types of patches:
      * Updates to the ``test_pages`` files for missed cases.
      * Documentation updates
      * SCSS updates
   * Submit a pull request!
   * Include a screen shot if it is a different look so others can give feedback without having to download and install the fork.

