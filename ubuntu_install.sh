#!/bin/sh

# Tested on Ubuntu 18.04
# git clone --recurse-submodules https://github.com/The-OpenROAD-Project/PCB-PR-App.git

export CXX=g++
./basic_depencencies.sh
pwd
ls
bash ./clean.sh
bash ./build.sh
