#!/bin/bash

cd $1
username=$whoami
echo "Current username is $USER"
echo "Current directory is $PWD"
echo "Home directory is $HOME"
echo ""
echo "--5 most recently modified directories with rwxrwxrwx --"
find . -type d -perm -777 | head -5

echo ""
echo "--Files in last 30-60 minutes"
find . -maxdepth 1 -type f -mmin +60 -mmin -30
echo ""
echo "======================================================================"
