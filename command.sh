printf "generate files\n"

opencv/build/bin/opencv_createsamples -info positive.dat -num 20000 -w 48 -h 24 -vec face.vec

mkdir -p "data"

printf "start training\n"
opencv/build/bin/opencv_traincascade -data model -vec face.vec -bg negative.dat -numPos 20000 -numNeg 5917 -numStages 10 -w 48 -h 24
