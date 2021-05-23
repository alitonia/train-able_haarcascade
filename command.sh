printf "generate files\n"

opencv/build/bin/opencv_createsamples -info positive.dat -num 20000 -w 20 -h 20 -vec face.vec

mkdir -p "data"

printf "start training\n"
opencv/build/bin/opencv_traincascade -data model -vec face.vec -bg negative.dat -numPos 10000 -numNeg 5917 -numStages 10 -w 20 -h 20 -precalcValBufSize 1024 -precalcIdxBufSize 2048 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -weightTrimRate 0.95 -acceptanceRatioBreakValue 0.00042
