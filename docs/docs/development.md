# Setting up development environment

To install command line tools go to the scripts/cli_shortcuts folder
and type `python setup.py develop`

This install a command line program called 'dj' (short for django because these started off as django shortcuts) that can bootstrap commands for Django and the whole program in general. For example `dj s`
loads the development server with the development settings as shown below.

To start a development server run

```
python manage.py runserver --settings=appcore.settings.development
```
