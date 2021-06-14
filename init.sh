mv ~/stepic_web_application ~/web
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/defualt
sudo /etc/init.d/nginx restart
