#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: TrucGiang
# DATE CREATED:        10.04.2024                         
# REVISED DATE:        10.04.2024
# PURPOSE: Create a function classify_images that uses the classifier function 

from classifier import classifier 
import os

def classify_images(images_dir, results_dic, model):
    for key_rs in results_dic:
        image_path = os.path.join(images_dir, key_rs)
        label = classifier(image_path, model)
        label = label.lower().strip()
        tr = results_dic[key_rs][0]   
        if tr in label:
            results_dic[key_rs].extend((label, 1))
        else:
            results_dic[key_rs].extend((label, 0))



