#! /bin/bash

source envvars.config
cd $SITE_DIR/..

cp bundle/jquery-ui-1.10.4.custom.zip cevido.com.br/static/
cd  cevido.com.br/static/
unzip jquery-ui-1.10.4.custom.zip
rm jquery-ui-1.10.4.custom.zip
