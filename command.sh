printf "generate files\n"

opencv/build/bin/opencv_createsamples -info positive.dat -num 20000 -w 48 -h 48 -vec face.vec

mkdir -p "data"

printf "start training\n"
opencv/build/bin/opencv_traincascade -data model -vec face.vec -bg negative.dat -numPos 17000 -numNeg 5917 -numStages 10 -w 48 -h 48 -featureType LBP -precalcValBufSize 1024 -precalcIdxBufSize 1024 -minHitRate 0.99 -maxFalseAlarmRate 0.5 -weightTrimRate 0.95 -acceptanceRatioBreakValue 0.00042
