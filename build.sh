rm -r build
rm -r ucsdpcb

mkdir build
mkdir ucsdpcb
touch ucsdpcb/__init__.py
cp util/check_output.py ucsdpcb

cd build
cmake ..
make
cd ..
sh create_shared_objs.sh
