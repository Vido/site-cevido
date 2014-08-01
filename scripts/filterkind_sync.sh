#! /bin/sh

cd ../cevido.com.br

sqlite3 db.sqlite3 'DROP TABLE filter_filterkind;'
python manage.py syncdb --noinput
python manage.py migrate
python manage.py loaddata ../scripts/fixtures/filter_filterkind.json
