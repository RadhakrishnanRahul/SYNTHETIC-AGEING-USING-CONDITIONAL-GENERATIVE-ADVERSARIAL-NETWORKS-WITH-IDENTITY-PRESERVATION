# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:36:14 2020

@author: Rahul
"""
#import numpy as np
from sklearn.model_selection import train_test_split
from os import listdir
from os.path import isfile, join

#import utils

IMAGE_PATH= "../new_images/"

file_train_0 = open("train_age_group_0.txt", "a")
file_train_1 = open("train_age_group_1.txt", "a")
file_train_2 = open("train_age_group_2.txt", "a")
file_train_3 = open("train_age_group_3.txt", "a")
file_train_4 = open("train_age_group_4.txt", "a")
file_train_all = open("train_all.txt", "a")
file_test_0 = open("test_age_group_0.txt", "a")
file_test_1 = open("test_age_group_1.txt", "a")
file_test_2 = open("test_age_group_2.txt", "a")
file_test_3 = open("test_age_group_3.txt", "a")
file_test_4 = open("test_age_group_4.txt", "a")
file_test_all = open("test_all.txt", "a")

onlyfiles = [f for f in listdir(IMAGE_PATH) if isfile(join(IMAGE_PATH, f))]
age_range_0 = []
age_range_1 = []
age_range_2 = []
age_range_3 = []
age_range_4 = []
for img_file in onlyfiles:
    if(img_file[0] == '1'):
        age_range_0.append(img_file)
    elif(img_file[0] == '2'):
        age_range_1.append(img_file)
    elif(img_file[0] == '3'):
        age_range_2.append(img_file)
    elif(img_file[0] == '4'):
        age_range_3.append(img_file)
    else:
        age_range_4.append(img_file)

train, test = train_test_split(age_range_0, test_size = 0.1)
for line in train:
    file_train_0.write(line + ' 0\n')
    file_train_all.write(line + ' 0\n')
for line in test:
    file_test_0.write(line + ' 0\n')
    file_test_all.write(line + ' 0\n')
    
train, test = train_test_split(age_range_1, test_size = 0.1)
for line in train:
    file_train_1.write(line + ' 1\n')
    file_train_all.write(line + ' 1\n')
for line in test:
    file_test_1.write(line + ' 1\n')
    file_test_all.write(line + ' 1\n')
    
train, test = train_test_split(age_range_2, test_size = 0.1)
for line in train:
    file_train_2.write(line + ' 2\n')
    file_train_all.write(line + ' 2\n')
for line in test:
    file_test_2.write(line + ' 2\n')
    file_test_all.write(line + ' 2\n')
    
train, test = train_test_split(age_range_3, test_size = 0.1)
for line in train:
    file_train_3.write(line + ' 3\n')
    file_train_all.write(line + ' 3\n')
for line in test:
    file_test_3.write(line + ' 3\n')
    file_test_all.write(line + ' 3\n')
    
train, test = train_test_split(age_range_4, test_size = 0.1)
for line in train:
    file_train_4.write(line + ' 4\n')
    file_train_all.write(line + ' 4\n')
for line in test:
    file_test_4.write(line + ' 4\n')
    file_test_all.write(line + ' 4\n')
    
        
