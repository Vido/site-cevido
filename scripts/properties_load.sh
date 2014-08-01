#!/bin/bash

source envvars.config
cd $SITE_DIR

rm db*
python manage.py syncdb --noinput
python manage.py migrate
python manage.py loaddata ../scripts/dev_real_estate_property.json
python manage.py loaddata ../scripts/dev_auth_users.json
