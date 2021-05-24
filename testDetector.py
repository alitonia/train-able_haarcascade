# Importing the libraries
import os
import cv2
from matplotlib import pyplot as plt
import HaarModelDetector as md

#Prepare model
detector = md.ModelDetector()
detector.prepare()

#Use model to predict 
test_image_path = 'anh_hoi_dong.jpg'
detected = detector.detect_with_path(test_image_path)

for (conf, x,y,w,h) in detected:
    print(conf, x,y,w,h)