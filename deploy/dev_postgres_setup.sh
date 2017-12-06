begin;
CREATE ROLE compass_webapp WITH LOGIN PASSWORD 'password';
CREATE ROLE compass_helpers WITH LOGIN PASSWORD 'password';
ALTER DATABASE compass_webapp OWNER TO root;
commit;

begin;
REVOKE CONNECT ON DATABASE compass_webapp_db FROM PUBLIC;

GRANT CONNECT
ON DATABASE compass_webapp_db
TO compass_webapp, compass_helpers;
commit;
