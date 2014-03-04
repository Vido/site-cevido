#! /bin/sh

cd ..

rm db*
python manage.py syncdb --noinput
python manage.py loaddata real_estate/fixtures/property.json
python manage.py loaddata scripts/dev_users.json

