#! /bin/bash

source envvars.config
cd $SITE_DIR/..

cp bundle/jquery-ui-1.10.4.custom.zip $SITE_DIR/static/
cd  $SITE_DIR/static/
unzip jquery-ui-1.10.4.custom.zip
rm jquery-ui-1.10.4.custom.zip
