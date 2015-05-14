#!/bin/sh
# This assumes you installed Plone on Nitrous.io using these instructions
# http://blog.dbain.com/2013/07/plone-quickstart-on-cloud-in-less-than.html

# download this file and run it with the following command
# sh plone-restart.sh

echo "Restarting Plone"
tmux kill-window -t 2
tmux kill-window -t 1

tmux new-window -t plone:1 -n 'Zeo' '~/workspace/zeocluster/bin/zeoserver fg'
tmux new-window -t plone:2 -n 'Client1' 'echo "restarting";~/workspace/zeocluster/bin/client1 fg'
 
tmux select-window -t plone:2
tmux -2 attach-session -t plone