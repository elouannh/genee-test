#!/bin/bash

all_missing_env_vars=()
check_env_var() {
  var_value=$(printf '%s\n' "${!1}")
  if [ -z "$var_value" ]; then
    all_missing_env_vars+=( "$1" )
  fi
}
check_env_var DB_USER
check_env_var DB_NAME
check_env_var DB_IP
check_env_var DB_PORT

if [ ${#all_missing_env_vars[@]} -ne 0 ]; then
    echo "Missing environment variables: ${all_missing_env_vars[@]}"
    exit 1
fi

while ! pg_isready -d "${DB_NAME}" -h "${DB_IP}" -p "${DB_PORT}" -U "${DB_USER}" -t 1; do
  echo "Waiting for postgres server ready to accept connections..."
  sleep 2
done

echo "Postgres server ready to accept connections, starting flask server"

export FLASK_APP=main.py

python app/main.py
