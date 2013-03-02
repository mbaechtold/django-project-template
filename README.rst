django-project-template
=======================

If you don't like to repeat yourself every time you create a new Django project, you definitely want to have a look
at the `--template` option of the `startproject` command introduced in Django 1.4.

This git repo holds my personal Django project layout template which allows me to start a new Django project in just
a few seconds.

Please consider this a pre-alpha release. Use it at your own peril.


Usage
-----

::

    django-admin.py startproject --template https://github.com/downloads/mbaechtold/django-project-template/latest.zip --extension py,md,gitignore,dist your_project_name <path_to_your_project>


Features
--------

This project template features a fully configured instance of the great `django-cms <http://www.django-cms.org>`_ and
is based heavily on the following list of great apps:

* Pillow (the repackaged PIL)
* South (for easy database migrations)
* easy-thumbnails
* django-bootstrap-toolkit
* django-extensions
* django-filer and cmsplugin-filer
* django-ganalytics


Planned features
----------------

* Write a `Getting started` guide for fellow developers ideally in the `docs` folder
* Sample templates including Twitter Bootstrap
* Advanced Django settings (multi-site and multi-environment)
* Logging settings for Sentry
* Fabric file for easy deployment
* Configure django-filer for its "secure media" feature


Good to know
------------

There are two symbols defined in the settings file:
* PROJECT_ROOT is the main directory of the project, i.e. the directory holding the docs, requirements, src, static and upload folder
* SOURCE_ROOT points to the `src` folder within PROJECT_ROOT


Author
------

Martin Bächtold made this. Feel free to contact me on `Twitter <http://twitter.com/mbaechtold>`_ or
`Github <https://github.com/mbaechtold>`_.


License
-------

You are free to use this software under the MIT License. See LICENSE file for details.