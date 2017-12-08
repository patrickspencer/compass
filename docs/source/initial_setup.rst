.. _development_setup:

Initial Setup
=============

Setting up development environment
----------------------------------

First, create the database `compass_webapp_db` yourself following the directions below.

Once the database has been created, run the following commands to run all the
migrations.

.. code:: bash

   python manage.py migrate

Create the first two users `leuler` and `jdoe` with the command

.. code:: bash

   py manage.py loaddata helpers/initial_fixtures.json

This creates a super user `leuler` with the password `password` and a
regular user `jdoe` with the password `password`.

To start a development server run

.. code:: bash

   python manage.py runserver

To start a production server run

.. code:: bash

   python manage.py runserver --settings=appcore.settings.production

To start a development server run

Initial database setup
----------------------

Install all system dependencies by running `bash
scripts/install_dependencies`. These
dependencies are for Debian\Ubuntu based systems.

Install pip dependencies by running `pip3 install -r requirements/development.txt`.

To starting postgres run

.. code:: bash

    postgres -D /usr/local/pgsql/data >logfile 2>&1 &

or

.. code:: bash

   pg_ctl start -l logfile

You can check is postgres is running by typing

.. code:: bash

   ps auxwww | grep postgres

You should see something like this:

.. code:: bash

   /Library/PostgreSQL/9.4/bin/postgres -D /Library/PostgreSQL/9.4/data

or

.. code:: bash

   postgres  8549  0.0  0.3 274196 24284 ?        S    22:26   0:00
   /usr/lib/postgresql/9.5/bin/postgres -D /var/lib/postgresql/9.5/main -c
   config_file=/etc/postgresql/9.5/main/postgresql.conf

Create database

.. code:: bash

   createdb compass_webapp_db

Create new role

.. code:: bash

   psql
   =# CREATE ROLE compass_webapp WITH LOGIN PASSWORD 'password';
   =# CREATE ROLE compass_helpers WITH LOGIN PASSWORD 'password';
   =# ALTER DATABASE compass_webapp OWNER TO root;

Grant all access to usernames from
`stackexchange <http://dba.stackexchange.com/questions/33943/granting-access-to-all-tables-for-a-user>`_

.. code:: bash

   REVOKE CONNECT ON DATABASE compass_webapp_db FROM PUBLIC;

   GRANT CONNECT
   ON DATABASE compass_webapp_db
   TO compass_webapp, compass_helpers;

Check database has been created with

.. code:: bash

   psql
   =# \list

Check user has been created with

.. code:: bash

   psql
   =# \du

Connect to postgres after install on Ubuntu
`Ubuntu postgres page <https://help.ubuntu.com/community/PostgreSQL>`_

.. code:: bash

   sudo -u postgres psql postgres

run ansible

.. code:: bash

   ansible-playbook site.yml

Production Setup
----------------

Follow all the steps for the initial setup above. Then from the base directory
run the following command

.. code:: bash

   sudo uwsgi --ini deploy/uwsgi.ini
