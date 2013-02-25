=======
Testing
=======

Since this project is only about look and feel, there is no automated testing. Instead we have created a set of HTML files to include all possible outcomes of each Django admin theme. These files are located in ``test_pages`` and are viewable in a browser as is. The have been modified to load their CSS and JavaScript from the ``../admintheme/static/`` directory.

Test Files
==========

change_form_success.html
------------------------

This file is the basic admin change form with:

* A success message, as if the record was just saved
* Every possible field
* Some collapsed fieldsets

changeform.html
---------------

An example ``auth.User`` model form with:

* An error message at the top
* An error message on the field with the error
* A submit row at the top and bottom

dashboard.html
--------------

A basic Django dashboard with several applications and models. Also includes the recent changes list.

delete_confirmation.html
------------------------

The page Django shows when confirming that you *really* want to delete that item.

login.html
----------

Django's login screen for the admin portion.

password_change.html
--------------------

The screen used to change your password while in the admin area.