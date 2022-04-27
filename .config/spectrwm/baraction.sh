#!/bin/bash
# baraction.sh for spectrwm status bar
# From http://wiki.archlinux.org/index.php/Scrotwm

while :; do

##############################
#	    UPDATES
##############################

updates() {
        UPD="$(cat /home/larry/.local/bin/updates.cache)"

        echo $UPD 
        
        sleep 600
}

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

weather=$(cat ~/.config/weather.txt | sed 25q | grep value | awk '{print $2 $3}' | sed 's/\"//g')
temp=$(cat ~/.config/weather.txt | grep temp_F | awk '{print $2}' | sed 's/\"//g' | sed 's/,//')

nocloud="盛"
cloud=""
lotempicon="  "
midtempicon="  "
hitempicon="  "

#print weather info
TEMP() {
    echo "$temp °"
}

tempicon() {
if [ "$temp" -gt 80 ]; then
	echo $hitempicon
elif [ "$temp" -ge 50 ] && [ "$temp" -le 79 ]; then
	echo $midtempicon
elif [ "$temp" -le 49]; then
	echo $lotempicon
fi
}

weathericon() {
if [[ "$weather" = "Clear" ]] || [[ "$weather" = "Sunny" ]]; then
	echo "$nocloud $weather"
else
	echo "$cloud $weather"
fi
}

################################

echo -e "  $(weathericon) $(tempicon) $(TEMP) $(volicon) $(vol) "
    
done
