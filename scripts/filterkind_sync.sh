#!/bin/bash

source envvars.config
cd $SITE_DIR

sqlite3 db.sqlite3 'DROP TABLE filter_filterkind;'
python manage.py syncdb --noinput
python manage.py migrate
python manage.py loaddata ../scripts/fixtures/filter_filterkind.json
