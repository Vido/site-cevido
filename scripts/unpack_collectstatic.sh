#! /bin/bash

source envvars.config
cd $SITE_DIR/..

cp bundle/collectstatic.zip $SITE_DIR/static/
cd  $SITE_DIR/static/
unzip collectstatic.zip
rm collectstatic.zip
