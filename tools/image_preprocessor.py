# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:59:15 2020

@author: Rahul
"""

from PIL import Image
from os import listdir
from os.path import isfile, join

IMAGE_PATH= "../CACD2000/"
NEW_IMAGE_PATH = "../new_images/"

onlyfiles = [f for f in listdir(IMAGE_PATH) if isfile(join(IMAGE_PATH, f))]

for img_file in onlyfiles:
    
    im = Image.open(IMAGE_PATH + img_file)
    im
    width,height = im.size
    new_width=128
    new_height=128
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2
    
    # Crop the center of the image
    im = im.crop((left, top, right, bottom))
    #im.show()
    
    im = im.resize((400,400), Image.ANTIALIAS)
    im.save(NEW_IMAGE_PATH + img_file, "JPEG");

#for img_file in onlyfiles:
    