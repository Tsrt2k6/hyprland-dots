#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

if [[ $TERM == "xterm-kitty" ]]; then
  fastfetch -l ~/.config/hypr/icons/GjztaEoboAARvBt-removebg.png --logo-height 15 --logo-padding-left 2 --logo-padding-right 3
  alias clean="clear;fastfetch -l ~/.config/hypr/icons/GjztaEoboAARvBt-removebg.png --logo-height 15 --logo-padding-left 2 --logo-padding-right 3"
fi
