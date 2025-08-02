#!/bin/bash

swww query
if [ $? -eq 1 ] ; then
	swww-daemon
fi

swww restore &
#hellwal -i $(swww query | grep -o -m 1 -P '(?<=image: ).*') -b 0.2 &
#swww img ~/Wallpapers/PrevImg.jpg --transition-type simple
