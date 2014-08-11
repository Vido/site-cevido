#!/bin/bash

source envvars.config
cd $SITE_DIR

# sqlite3 db.sqlite3 'DROP TABLE filter_filterkind;' # Dev
python manage.py syncdb --noinput
python manage.py migrate
python manage.py loaddata cevido/initial_data.json
python manage.py loaddata filter/fixtures/filter_filterkind.json
python manage.py loaddata real_estate/fixtures/real_estate_default_gallery.json

sqlite3 db.sqlite3 'SELECT * FROM filter_filterkind;'
sqlite3 db.sqlite3 'SELECT * FROM auth_user;'
