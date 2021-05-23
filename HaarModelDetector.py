# Importing the libraries
import os
import cv2
from matplotlib import pyplot as plt

class ModelDetector:
    def prepare(self):
        self.face_cascade = cv2.CascadeClassifier('model/cascade.xml')

    # Defining a function that will do the detections
    def detect(self, frame):
        return self.face_cascade.detectMultiScale(frame, 1.3, 5)
        