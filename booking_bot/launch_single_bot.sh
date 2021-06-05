#! /bin/bash

printf "Launching bot...\n"
printf "Press CTRL-C to cancel\n"
(python3 bot.py > /dev/null)&

trap ctrl_c INT
function ctrl_c() {
    kill -9 $(ps | grep python3 | awk '{print $1}')
    exit 1
}

while :
do
    sleep 1
done
