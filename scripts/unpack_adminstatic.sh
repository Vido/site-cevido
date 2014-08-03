#! /bin/bash

source envvars.config
cd $SITE_DIR/..

cp bundle/admin.zip cevido.com.br/static/
cd  cevido.com.br/static/
unzip admin.zip
rm admin.zip
