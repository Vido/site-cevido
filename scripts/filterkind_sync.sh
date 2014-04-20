#! /bin/sh

cd ..

sqlite3 db.sqlite3 'DROP TABLE filter_filterkind;'
python manage.py syncdb --noinput
python manage.py migrate
python manage.py loaddata filter/fixtures/dev_filterkind.json
