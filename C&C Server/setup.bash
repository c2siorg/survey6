#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
sudo cp server.service /etc/systemd/system/survey6_server.service


function cncserver 
{ 
    if [ -z "$1" ];
    then
        echo "Enter a command: start / stop"
    elif [ "$1" = "start" ]; 
    then 
        systemctl start survey6_server
    elif [ "$1" = "stop" ]; 
    then 
        systemctl stop survey6_server
    else
        echo "Command not supported"
    fi 
}

alias cncserver=cncserver

