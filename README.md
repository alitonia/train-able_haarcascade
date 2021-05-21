## HaarCascade face detection

### What is this

The repo shows steps to train a face detection model with haar cascade of OpenCv

### Steps

* download face annotation, face training images, extract, put in root of this repo
  from http://shuoyang1213.me/WIDERFACE/

* download non-face training images, extract, put at root of this repo
  from https://www.kaggle.com/prasunroy/natural-images

* run `precommand.sh`
* `pip install -r requirements.txt`
* `python generate.py`
* run `command.py`
* run __HaarCascade.ipynb__
