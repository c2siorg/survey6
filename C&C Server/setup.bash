#!/bin/bash


# Installation of requirements in virtual env
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt


# Creating a service 
sudo cp server.service /etc/systemd/system/survey6_server.service

systemctl daemon-reload

# Aliasing 
cat cnc_server.bash_aliases >> ~/.bash_aliases 

source ~/.bashrc