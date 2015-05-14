#!/bin/sh
# This assumes you installed Plone on Nitrous.io using these instructions
# http://blog.dbain.com/2013/07/plone-quickstart-on-cloud-in-less-than.html

# download this file and run it with the following command
# sh plone-builddev.sh

echo "running buildout with default buildout.cfg"
~/workspace/zeocluster/bin/buildout -c ~/workspace/zeocluster/buildout.cfg