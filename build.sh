rm -r build
rm -r ucsdpcb

mkdir build
mkdir ucsdpcb
touch ucsd/__init__.py

cd build
cmake ..
make
cd ..
sh create_shared_objs.sh
