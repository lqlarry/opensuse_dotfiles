#!/bin/bash
# baraction.sh for spectrwm status bar
# From http://wiki.archlinux.org/index.php/Scrotwm

while :; do

##############################
#	    VOLUME
##############################

volicon() {
    VOLONOFF="$(amixer -D pulse get Master | grep Left: | sed 's/[][]//g' | awk '{print $6}')"

    VOLON=""
    VOLOFF="ﱝ"

    if [ "$VOLONOFF" = "on" ]; then
        echo "$VOLON"
    else
        echo "$VOLOFF"
    fi
    sleep 0.5
}

vol() {
    VOL="$(amixer -D pulse get Master | grep Left: | sed 's/[][]//g' | awk '{print $5}')"

    echo "$VOL" 
}

##############################
#	    WEATHER
##############################

weather() {
        $WEA="$(awk '{print $0} '/home/larry/.local/bin/weather.txt)"

        echo "$WEA" 

}

################################

echo -e "$(WEA) $(volicon) $(vol) "
    
done
