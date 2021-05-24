# Importing the libraries
import os
import cv2
from matplotlib import pyplot as plt

class ModelDetector:
    face_cascade = None
    def prepare(self):
        self.face_cascade = cv2.CascadeClassifier('model/cascade.xml')

    # Defining a function that will do the detections
    def detect(self, frame):
        detected = self.face_cascade.detectMultiScale3(frame, 1.3, 5, outputRejectLevels = True)
        rects = detected[0]
        weights = detected[2]
        conf = weights[:,0]/max(weights[:,0])
        
        returnList = []
        for i in range(conf.size):
            x,y,w,h = rects[i]
            returnList.append([conf[i],x,y,w,h])
        return returnList
    
    def detect_with_path(self, path_to_image):
        frame = cv2.imread(path_to_image)
        return self.detect(frame)