#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static. It must:
DIR="/etc/nginx/sites-available/default"
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Testing HTML" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo useradd ubuntu
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '52i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $DIR
sudo service nginx start
sudo service nginx restart
sudo service nginx reload
