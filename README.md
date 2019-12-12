# PCB-PR-App

Top-level app for PCB P&R flow

### Prerequisites

- GCC >=4.8
- SWIG >= 2.0
- Boost >= 1.6

### Installing

create a top-level bin directory

```
mkdir bin
cd bin.
```

run cmake and make to build submodules

```
cmake ..
make
````

compile shared objects and swig libraries

```
sh create_shared_obs.sh 
````

ensure you can import the libraries

```
cd lib
python
>>> import PcbDB, PcbRouter, PcbPlacer
````

alternatively, call the test python placement program:

```
mv test_flow.py lib/
cd lib/
python test_flow.py
```

have fun!

## Running the tests

## Current issues

- Tested in CentOS 6
- Linking shared object files after swig compilation currently fails on OSX

## License

  * BSD-3-clause License [[Link]](LICENSE)
