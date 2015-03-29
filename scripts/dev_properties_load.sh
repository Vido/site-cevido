#!/bin/bash

source envvars.config
cd $SITE_DIR

python manage.py loaddata real_estate/fixtures/city_fixture.json
python manage.py loaddata real_estate/fixtures/owner_fixture.json
python manage.py loaddata real_estate/fixtures/property_fixture.json
