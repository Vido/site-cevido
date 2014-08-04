#! /bin/bash

source envvars.config
cd $SITE_DIR/..

cp bundle/admin.zip $SITE_DIR/static/
cd  $SITE_DIR/static/
unzip admin.zip
rm admin.zip
