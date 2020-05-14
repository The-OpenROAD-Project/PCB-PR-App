# Tested on Ubuntu 18.04
# git clone --recurse-submodules https://github.com/The-OpenROAD-Project/PCB-PR-App.git

export CXX=g++
apt-get update
apt-get install -y swig
apt-get install -y libboost-all-dev
apt-get install -y cmake
apt install -y python3-pip
pip3 install docopt
source clean.sh
source build.sh
