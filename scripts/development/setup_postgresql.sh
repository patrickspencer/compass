# run this script as postgres user: sudo -u postgres bash setup_postgresql.sh

# libpg-dev is for psycopg2
# libffi-dev is for bcrypt
sudo apt-get install -y build-essential python3-pip \
    python3-dev postgresql postgresql-contrib libpq-dev libffi-dev

# postgres
createdb compass_dev_db
psql -c "CREATE ROLE compass_webapp WITH LOGIN PASSWORD 'password'"
psql -c "CREATE ROLE compass_helpers WITH LOGIN PASSWORD 'password'"

pip install -r requirements/development.txt

python manage.py migrate --settings=config.settings.development
python manage.py collectstatic --settings=config.settings.development

