# Importing the libraries
import os
import cv2
from matplotlib import pyplot as plt
import ModelDetector as md

#Prepare model
detector = md.ModelDetector()
detector.prepare()

#Use model to predict 
test_image_path = 'anh_hoi_dong.jpg'
img = cv2.imread(test_image_path)
detected = detector.detect(img)

#Write to new file named "resultbb.txt"
file_path = "resultbb.txt"
with open(file_path, 'w') as file:
    for (x,y,w,h) in detected:
        file.write(str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n')
        