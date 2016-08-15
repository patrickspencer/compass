# Setting up development environment

To install command line tools go to the scripts/cli_shortcuts folder
and type `python setup.py develop`

This install a command line program called 'dj' (short for django because these
started off as django shortcuts) that can bootstrap commands for Django and the
whole program in general. For example `dj s` loads the development server with
the development settings as shown below.

To start a development server run

```
python manage.py runserver
```

To start a production server run
```
python manage.py runserver --settings=appcore.settings.production
```

## Postgres

Install all system dependencies by running `bash scripts/install_dependencies`. These
dependencies are for Debian\Ubuntu based systems.

Install pip dependencies by running `pip3 install -r
requirements/development.txt`.

To starting postgres run
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
or
```
postgres  8549  0.0  0.3 274196 24284 ?        S    22:26   0:00 /usr/lib/postgresql/9.5/bin/postgres -D /var/lib/postgresql/9.5/main -c config_file=/etc/postgresql/9.5/main/postgresql.conf
```

Create database
```
createdb compass_webapp_db
```

create new role
```
psql
=# CREATE ROLE compass_webapp WITH LOGIN PASSWORD 'password';
=# CREATE ROLE compass_helpers WITH LOGIN PASSWORD 'password';
=# ALTER DATABASE compass_webapp OWNER TO root;
```

Grant all access to usernames from [stackexchange](http://dba.stackexchange.com/questions/33943/granting-access-to-all-tables-for-a-user):
```
REVOKE CONNECT ON DATABASE your_database FROM PUBLIC;

GRANT CONNECT
ON DATABASE compass_webapp_db
TO compass_webapp, compass_helpers;
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

Connect to postgres after install on Ubuntu
from [Ubuntu postgres page](https://help.ubuntu.com/community/PostgreSQL)
```
sudo -u postgres psql postgres
```

run ansible
```
ansible-playbook site.yml
```

Build docker image from Dockerfile:
cd into directory with docker file and run:
```
docker build -t compass_webapp .
```

