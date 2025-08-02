#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [[ $TERM == "linux" && $(tty) == "/dev/tty1" ]]; then
exec Hyprland &> /dev/null
#exec startplasma-wayland
exec powertop --auto-tune
fi
