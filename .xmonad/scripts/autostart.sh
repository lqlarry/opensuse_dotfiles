xrandr --output HDMI-1 --same-as LVDS-1 &
nitrogen --restore &
picom --config $HOME/.config/picom/picom.conf &
sleep 5 & /usr/libexec/polkit-gnome-authentication-agent-1 &
sleep 10 & xset s 0 0 &
sleep 10 & xset s noblank &
sleep 10 & xset dpms 0 0 0 &

