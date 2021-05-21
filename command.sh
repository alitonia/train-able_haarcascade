opencv/build/bin/opencv_createsamples -info generated/positive.dat -num 20000 -w 48 -h 24 -vec generated/face.vec

mkdir -p "data"

opencv/build/bin/opencv_traincascade -data model -vec generated/face.vec -bg generated/negative.dat -numPos 20000 -numNeg 5917 -numStages 10 -w 48 -h 24
