#! /bin/sh

cd ..

rm db*
python manage.py syncdb --noinput
python manage.py loaddata r
