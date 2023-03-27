git clone --recursive https://github.com/microsoft/LightGBM
cd LightGBM
rm -rf .github
mkdir build
cd build
cmake -DUSE_GPU=0 -DCMAKE_C_FLAGS="-arch arm64" -DCMAKE_CXX_FLAGS="-arch arm64" ..
make -j4

cd ../python-package
pipenv run python setup.py install --precompile

pipenv install numpy scipy

