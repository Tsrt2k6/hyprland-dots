#!/usr/bin/env bash

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

current="$(swww query | grep -o -m 1 -P '(?<=image: ).*')"
files=($(find "${SCRIPT_DIR}"/wallpapers/ -type f))
files=(${files[@]/$current})

if [ ${#files[@]} -ge 1 ]; then
  random="${files[RANDOM % ${#files[@]}]}"
  
  swww img "${random}" --resize crop --transition-type none
  #swww img "${random}" --resize crop --transition-type simple --transition-step 90 --transition-duration 1.2 --transition-fps 60 &
  #swww img "${random}" --resize fit --transition-bezier 0,0,1,1 --transition-type grow --transition-duration .7 --transition-fps 90 --invert-y --transition-pos "$( hyprctl cursorpos )"

  #wal -n -i "${random}" --backend fast-colorthief --cols16 lighten -b "#000000" &
  
  hellwal -i "${random}" -b 0.3 & 
  
  #convert ${random} -resize 720x -quality 50% ~/Wallpapers/rofi.jpg
  #cp -f ${random} ~/Wallpapers/PrevImg.jpg

  kill $(pgrep waybar)
  nohup waybar > /dev/null 2>&1 &
  echo "waybar reloaded!"

fi
