#!/bin/sh
# This assumes you installed Plone on Nitrous.io using these instructions
# http://blog.dbain.com/2013/07/plone-quickstart-on-cloud-in-less-than.html

# download this file and run it with the following command
# this shows the activites on client1 (useful for debugging)
# sh plone-debug.sh

tmux select-window -t plone:2
tmux -2 attach-session -t plone