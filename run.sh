#!/bin/bash

curl https://raw.githubusercontent.com/zooper/pathalerts/master/pathalerts.py -o /application/pathalerts.py
touch /log/log.txt
python /application/pathalerts.py
