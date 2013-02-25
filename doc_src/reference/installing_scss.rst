======================
Using SASS and Compass
======================


Installing SASS and Compass
===========================

SASS_ and Compass_ are built in Ruby, but you don't need to know any Ruby to use them.

#. From the command line, install SASS::

   sudo gem install sass

#. Then install compass::

   sudo install compass


.. _SASS: http://sass-lang.com/
.. _Compass: http://compass-style.org/


Compiling the style sheets
==========================

Compass can watch a directory for changes and automatically update the generated CSS. From the root ``django-admintheme`` directory (the same level where the ``README.txt`` and ``setup.py`` files are) run this command::

   compass watch admintheme/static/admin/scss

Every time you make a change to a source file, it will update the CSS.