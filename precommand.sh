printf "cloning opencv source\n"
git clone https://github.com/opencv/opencv.git

printf "change opencv to 3.4\n"
#https://github.com/opencv/opencv/issues/13231 😑
cd opencv && git checkout 3.4 && cd ..

printf "build from source\n"
cd opencv || exit
mkdir -p build
cd build || exit

cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON ..

make -j7

printf "install binary\n"
sudo make install

mkdir -p log
mkdir -p model
