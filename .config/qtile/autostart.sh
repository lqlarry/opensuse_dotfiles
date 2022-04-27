#!/bin/sh
xrandr --output HDMI-1 --same-as LVDS-1 &
picom &
xset s off &
xset -dpms &
numlockx &
dunst &
nm-applet &
nitrogen --restore &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
