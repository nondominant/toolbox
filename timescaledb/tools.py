#the following is taken from https://docs.timescale.com/install/latest/self-hosted/installation-source/

#if postgress is not installed, do that 
sudo pacman -S postgresql

#ensure postgres user exists
sudo passwd -Sa

#self hosted timescale db install
git clone https://github.com/timescale/timescaledb.git

cd timescaledb

git checkout 2.5.1

./bootstrap

cd build && make

make install

#become postgres user
su postgres

#configure
psql -c "SHOW config_file;"

echo "shared_preload_libraries = 'timescaledb'" >> ~/path/postgres.conf 

sudo systemctl stop postgresql
sudo systemctl start postgresql

# setup for TimeScaleDB
#attach
psql -h localhost
#create
CREATE database example;
#connect
\c example
#add extension
CREATE EXTENSION IF NOT EXISTS timescaledb;
#attach (as postgres user already)
psql -h localhost -d example
#attach (as another user)
psql -U postgres -h localhost -d example

#Now that you have your first TimescaleDB database up and running, you can check out the TimescaleDB section in our documentation, and find out what you can do with it.
# https://docs.timescale.com/timescaledb/latest/
#
#If you want to work through some tutorials to help you get up and running with TimescaleDB and time-series data, check out our tutorials section.
# https://docs.timescale.com/timescaledb/latest/tutorials/



