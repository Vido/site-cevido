#!/bin/bash

source envvars.config
cd $SITE_DIR

rm db*
python manage.py syncdb --noinput
python manage.py migrate
python manage.py loaddata ../scripts/fixtures/dev_initial_data.json
#python manage.py loaddata real_estate/fixtures/real_estate_default_gallery.json
