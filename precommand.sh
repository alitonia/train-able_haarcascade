# goto http://shuoyang1213.me/WIDERFACE/
# download face annotation, put in root of this repo
# run generate.py
# then

git clone https://github.com/opencv/opencv.git

#https://github.com/opencv/opencv/issues/13231 😑
cd opencv && git checkout 3.4 && cd ..

#git clone https://github.com/opencv/opencv_contrib.git

cd opencv
mkdir -p build
cd build


cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..

make -j7

sudo make install

mkdir -p log
mkdir -p generated
mkdir -p model