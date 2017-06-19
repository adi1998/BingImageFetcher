#!/bin/bash

#Stuff for proper working of cronjob
PID=$(pgrep -o gnome-session)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

#Call the main script
python /home/gr33n5h4d0w/automate_things/bing_wallpaper/mainscript.py
