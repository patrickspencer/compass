# Setting up development environment

To install command line tools go to the scripts/cli_shortcuts folder
and type `python setup.py develop`

This install a command line program called 'dj' (short for django because these
started off as django shortcuts) that can bootstrap commands for Django and the
whole program in general. For example `dj s` loads the development server with
the development settings as shown below.

To start a development server run

```
python manage.py runserver --settings=appcore.settings.development
```

starting postgres
```
postgres -D /usr/local/pgsql/data >logfile 2>&1 &
```
or
```
pg_ctl start -l logfile
```

You can check is postgres is running by typing 
```
ps auxwww | grep postgres
```
You should see something like this:
```
/Library/PostgreSQL/9.4/bin/postgres -D /Library/PostgreSQL/9.4/data
```
Create database
```
createdb compass_webapp
```
create new role
```
psql  
=# CREATE ROLE root WITH LOGIN PASSWORD 'password' SUPERUSER;
=# ALTER DATABASE compass_webapp OWNER TO root;
```
Check database has been created with
```
psql  
=# \list
```
Check user has been created with 
```
psql  
=# \du
```
