#!/bin/sh
# This command will create a backup of the PostgreSQL data directory and store it in the
# sudo cp -R /var/lib/postgresql /var/lib/postgresql_backup

sudo apt-get -y update 
sudo apt-get -y install net-tools 
sudo apt-get -y install postgresql-15-postgis-3
sudo systemctl start postgresql
sudo systemctl enable postgresql
dpkg -l | grep postgresql


# sudo vi /etc/postgresql/15/main/postgresql.conf
# listen_addresses = 'localhost' --> listen_addresses = '*'

# sudo vi /etc/postgresql/15/main/pg_hba.conf

# IPv4 local connections:
# host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
# host    all             all             ::1/128                 scram-sha-256

# IPv4 local connections:
# host    all             all             0.0.0.0/0               md5
# IPv6 local connections:
# host    all             all             ::0/0                   md5

# sudo systemctl restart postgresql
# 

# sudo -i -u postgres
# \q -> to exit
# psql
# \conninfo
# \du ->check how many users
# psql -c "ALTER USER postgres WITH PASSWORD '';"

# sudo systemctl restart postgresql