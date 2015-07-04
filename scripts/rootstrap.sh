#!/usr/bin/env bash

apt-get update
apt-get upgrade -y
apt-get install -y python-pip

cd /vagrant
python setup.py install
