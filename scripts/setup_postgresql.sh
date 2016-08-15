createdb compass_webapp_db
psql -c "CREATE ROLE compass_webapp WITH LOGIN PASSWORD 'password'"
psql -c "CREATE ROLE compass_helpers WITH LOGIN PASSWORD 'password'""
