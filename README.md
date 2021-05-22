## HaarCascade face detection

### What is this

The repo shows steps to train a face detection model with haar cascade of OpenCv

### Required environment

* Linux
* Installed `python`, `cmake`, `make`

### Prepare repo (run only one time)

* download face annotation, face training images, extract, put in root of this repo
  from http://shuoyang1213.me/WIDERFACE/

* download non-face training images, extract, put at root of this repo
  from https://www.kaggle.com/prasunroy/natural-images

* run `precommand.sh`
* `pip install -r requirements.txt`

### Start training

* `python generate.py`
* run `command.py`
* run __HaarCascade.ipynb__

### Details

* Your model will be at __model/cascade.xml__