#!/bin/bash

cd ..
source ~/tflite/bin/activate
cd examples/lite/examples/object_detection/raspberry_pi
python detecttest.py

deactivate

cp testop.txt /home/gourav/FYP


cd ..
cd ..
cd ..
cd ..
cd ..
cd FYP
python vcma.py