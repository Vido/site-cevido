#! /bin/bash

source envvars.config
touch $WSGI_FILE
touch $SITE_DIR"/PRODUCTION"

# Update Log
cp $SITE_DIR"/static/error.log" $SITE_DIR"/static/error.txt"
