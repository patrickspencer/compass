Django shell shortcuts
======================

Django shell shortcuts

Usage
-----

This is a fork of `https://github.com/jgorset/django-shortcuts <https://github.com/jgorset/django-shortcuts>`_.

Django shell shortcuts installs a ``dj`` binary that proxies
Django's ``manage.py`` and ``django-admin.py`` scripts.

::

    $ dj <command or shortcut>

    $ cd any/project/subdirectory
    $ dj <command or shortcut>

Requirements
------------

Some commands require additional packages

+ Django Command Extensions


Shortcuts
---------

::

    # Django
    'c'  : 'collectstatic',
    's'  : 'runserver',
    'sd' : 'syncdb',
    'sp' : 'startproject',
    'sa' : 'startapp',
    't'  : 'test',

    # Shell
    'd'  : 'dbshell',
    's'  : 'shell',

    # Auth
    'csu': 'createsuperuser',
    'cpw': 'changepassword',

    # Migrations
    'sh'  : 'migrate',
    'sm' : 'schemamigration',

    # Django Extensions
    'sk' : 'generate_secret_key',
    'rdb': 'reset_db',
    'rp' : 'runserver_plus',
    'shp': 'shell_plus',
    'url': 'show_urls',
    'gm' : 'graph_models',
    'rs' : 'runscript'

Installation
------------

::

    $ python setup.py install
