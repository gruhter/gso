#!/bin/sh
# This assumes you installed Plone on Nitrous.io using these instructions
# http://blog.dbain.com/2013/07/plone-quickstart-on-cloud-in-less-than.html

# download this file and run it with the following command
# sh plone-stop.sh

tmux kill-window -t 2
tmux kill-window -t 1

echo "Plone has been stopped"