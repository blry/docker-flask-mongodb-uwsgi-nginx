#!/bin/bash

echo "UWSGI container is running"

MONGO_INITDB_ROOT_PASSWORD=$(cat $MONGO_INITDB_ROOT_PASSWORD_FILE) \
uwsgi --ini /etc/uwsgi/uwsgi.ini
