# Compass-python

This is an experimental course management tool written in python.

The app is laid out like this:

- Backend: Django
- Front end: sass, js
- Database: sqlite3 (Postgresql in the future)
- Caching: none (Redis or Memcache in the future)

Folder structure

```
├── deploy/
├── docs/
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   ├── docs.txt
│   └── production.txt
└── webapp/
    ├── appcore/
    ├── appstudent/
    ├── appstaff/
    ├── assets/
    ├── manage.py
    ├── templates/
    ├── tests/
    └── tmp/
```


```
  deploy/
    Setup scripts for environment

  docs/
    App documentation

  requirements/
    App dependencies 

  scripts/
    Command line helper scripts

  webapp/
    The source code for the web app. 
    Contains backend and frontend (in assets/ folder) components.
```

The deploy folder has Ansible files for setting up the development/production
environment.

# Setup

To install dependencies either run `pip install -r requirements/{ENV}.txt`
where `{ENV}` is either `production` or `development` depending on your
environment. For example, if you are developing run `pip install -r
requirements/development.txt`

Then run 

```
cd webapp  
python manage.py migrate --settings=appcore.settings.{ENV}
python manage.py collectstatic --settings=appcore.settings.{ENV}
```

Finally, to run the server run

`python manage.py runserver --settings=appcore.settings.{ENV}`
