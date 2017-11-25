# run setup_postgresql.sh before running this script

# libpg-dev is for psycopg2
# libffi-dev is for bcrypt
sudo apt-get install -y \
    build-essential \
    python3-pip \
    python3-dev \
    postgresql \
    postgresql-contrib \
    libpq-dev \
    libffi-dev

# requirements/ should be two folders down from this folder
pip3 install -r ../../requirements/development.txt

python3 ../../webapp/manage.py makemigrations --settings=config.settings.development
python3 ../../webapp/manage.py migrate --settings=config.settings.development
