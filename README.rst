django-project-template
=======================

If you don't like to repeat yourself every time you create a new Django project, you definitely want to have a look
at the `--template` option of the `startproject` command introduced in Django 1.4.

This git repo holds my personal Django project layout template which allows me to start a new project in just a few seconds.

Please consider this a pre-alpha release. Use it at your own peril.

Apps and helpers
----------------

Configuration is provided for the following apps (in alphabetic order):

* Fabric
* Pillow (instead of PIL)
* South
* cmsplugin-filer
* django-cms
* django-classy-tags
* django-bootstrap-toolkit
* django-extensions
* django-filer
* django-ganalytics
* django-mptt
* django-sekizai

Usage
-----

::

    django-admin.py startproject --template https://github.com/downloads/mbaechtold/django-project-template/latest.zip --extension py,md,gitignore,dist your_project_name


Planned features
----------------

* Fully configured Django project powered by django-cms ✓
* Sample templates including Twitter Bootstrap
* Advanced Django settings (multi-site and multi-environment)
* Logging settings for Sentry
* Fabric file for easy deployment

Author
------

Martin Bächtold made this. Please feel free to contact me on `Twitter <http://twitter.com/mbaechtold>`_ or
`Github <https://github.com/mbaechtold>`_.

License
-------

You can use this under the MIT License. See LICENSE file for details.