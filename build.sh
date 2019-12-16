rm -r build
rm -r lib

mkdir build
mkdir lib

cd build
cmake ..
make
cd ..
sh create_shared_objs.sh
