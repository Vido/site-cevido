#! /bin/bash

source envvars.config
cd $SITE_DIR

find -name '*.py' -print0 | xargs -r0 sed -e 's/[[:blank:]]\+$//' -i
find -name '*.js' -print0 | xargs -r0 sed -e 's/[[:blank:]]\+$//' -i
find -name '*.css' -print0 | xargs -r0 sed -e 's/[[:blank:]]\+$//' -i
find -name '*.html' -print0 | xargs -r0 sed -e 's/[[:blank:]]\+$//' -i
