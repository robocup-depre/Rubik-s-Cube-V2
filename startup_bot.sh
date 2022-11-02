#!/bin/sh
# startup.bot.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd home/pi/Rubik
python3 Bot.py
cd /
