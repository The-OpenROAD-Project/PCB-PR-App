# Tested on Ubuntu 18.04
# git clone --recurse-submodules https://github.com/The-OpenROAD-Project/PCB-PR-App.git

export CXX=g++
sudo apt-get update
sudo apt-get install -y swig
sudo apt-get install -y libboost-all-dev
sudo apt-get install -y cmake
sudo apt install -y python3-pip
pip3 install docopt
source clean.sh
source build.sh
