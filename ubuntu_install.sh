# Tested on Ubuntu 18.04
# git clone --recurse-submodules https://github.com/The-OpenROAD-Project/PCB-PR-App.git

export CXX=g++
apt-get update
apt-get install -y swig
apt-get install -y libboost-all-dev
apt-get install -y cmake
apt-get install -y git
apt install -y python3-pip
pip3 install docopt
pwd
ls
bash ./clean.sh
bash ./build.sh
