#!/bin/sh

#Start DB servers
memcachedb -p21201 -d -f ~/wrpp_db/db0/wrpp1.db -H ~/wrpp_db/db0/ -P ~/wrpp_db/db0/logs/0.pid
memcachedb -p21202 -d -f ~/wrpp_db/db1/wrpp1.db -H ~/wrpp_db/db1/ -P ~/wrpp_db/db1/logs/1.pid

#Start Servers
python src/server.py 0 &
python src/server.py 1 &

#Start LoadBalancer
python src/loadBalancer.py &
 
