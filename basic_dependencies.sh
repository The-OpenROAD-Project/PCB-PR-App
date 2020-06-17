#!/bin/sh
# Install basic depencencies on Ubuntu 18.04
apt-get update
apt-get install -y swig
apt-get install -y libboost-all-dev
apt-get install -y cmake
apt-get install -y git
apt install -y python3-pip
pip3 install docopt
