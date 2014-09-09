#! /bin/bash

set -e

source envvars.config
source info.txt

NOW=$(date +"%Y-%m-%d")
ZIPFILE=cevido-$NOW.zip
HOSTDIR=/home/cevido/www/site-cevido/
SSHOPTS="-o StrictHostKeyChecking=no"
read -s -p "PASSWORD: " SSHPASS
echo
export SSHPASS

sshpass -e ssh $SSHOPTS $SSH_HOST << EOF
cd $HOSTDIR
zip -r scripts/$ZIPFILE cevido_com_br
EOF

sshpass -e scp $SSHOPTS $SSH_HOST:/home/cevido/www/site-cevido/scripts/$ZIPFILE ./$ZIPFILE

sshpass -e ssh $SSHOPTS $SSH_HOST << EOF
cd $HOSTDIR
rm scripts/$ZIPFILE
EOF

unset SSHPASS
