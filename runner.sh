#!/bin/sh
# This (too) simple script is prepared to start 1 Load Balancer,
# two DB insatnces, and two Application Servers instances.

#Create DBs directories
mkdir ~/wrpp_db/
mkdir ~/wrpp_db/db0/
mkdir ~/wrpp_db/db0/logs/
mkdir ~/wrpp_db/db1/
mkdir ~/wrpp_db/db1/logs/

#Remove DBs
# rm -rf ~/wrpp_db/

#Start DB servers
memcachedb -p21201 -d -f ~/wrpp_db/db0/wrpp1.db -H ~/wrpp_db/db0/ -P ~/wrpp_db/db0/logs/0.pid
memcachedb -p21202 -d -f ~/wrpp_db/db1/wrpp1.db -H ~/wrpp_db/db1/ -P ~/wrpp_db/db1/logs/1.pid

#Start Servers
python src/server.py 0 &
python src/server.py 1 &

#Start LoadBalancer
python src/loadBalancer.py &
 
