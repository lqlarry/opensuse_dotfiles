#!/bin/sh

BROWSER="google-chrome-stable"

declare -a options=(

"1 - https://www.youtube.com/feed/subscriptions"
"2 - https://mail.google.com/mail/u/0/#inbox"
"3 - https://wiki.archlinux.org/title/Main_page"
"4 - https://github.com/"
"5 - https://stackexchange.com/"
"quit"

)

choice=$(printf '%s\n' "${options[@]}" | rofi -dmenu -i -l 20 -p 'Bookmarks')

if [[ "$choice" == quit ]]; then
        echo "Program Terminated."  && exit 1
elif [ "$choice" ]; then
        cfg=$(printf '%s\n' "${choice}" | awk '{print $NF}')
        $BROWSER "$cfg"
else 
        echo "Program Terminated." && exit 1
fi


