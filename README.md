# PCB-PR-App

Top-level app for PCB P&R flow

### Prerequisites

- GCC >=4.8
- G++ >= 4.8
```
export CXX=g++
```
- SWIG >= 2.0
```
sudo apt-get update
sudo apt-get install swig
```
- Boost >= 1.6
```
sudo apt-get update
sudo apt-get install libboost-all-dev
```
- CMake >= 3.1
```
sudo apt-get update
sudo apt-get install cmake
```

### Installing

Clone
```
git clone --recurse-submodules https://github.com/The-OpenROAD-Project/PCB-PR-App.git
```

Run the build script:
```
cd PCB-PR-App
source build.sh
```

Run the test script:
```
python3 test_flow.py
```

Have fun!

## Running the tests

## Current issues

- Tested on CentOS 6
- Tested on Ubuntu 18.04
- Linking shared object files after swig compilation currently fails on OSX. Docker is a good workaround on OSX.

## License
  * BSD-3-clause License [[Link]](LICENSE)
