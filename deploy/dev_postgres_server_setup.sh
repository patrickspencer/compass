#!/bin/bash
# set -e
# set -u

export DBHOST=$1
psql \
  -X \
  -h localhost \
  -f dev_postgres_setup.sql \
  --echo-all \
  --set AUTOCOMMIT=off \
  --set ON_ERROR_STOP=on \
   mydatabase

   psql_exit_status = $?

   if [ $psql_exit_status != 0 ]; then
     echo "psql failed while trying to run this sql script" 1>&2
     exit $psql_exit_status
   fi

   echo "sql script successful"
exit 0
