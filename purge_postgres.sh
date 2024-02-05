#!/bin/sh
# This command will create a backup of the PostgreSQL data directory and store it in the
# sudo cp -R /var/lib/postgresql /var/lib/postgresql_backup
sudo systemctl disable postgresql
sudo apt-get -y purge postgresql-15
sudo apt-get -y purge postgresql-client-common
sudo apt-get -y purge postgresql-common
sudo apt-get -y autoremove
# echo "******************"
sudo rm -rf /etc/postgresql
sudo rm -rf /var/lib/postgresql
sudo rm -rf /var/lib/postgresql
dpkg -l | grep postgresql

