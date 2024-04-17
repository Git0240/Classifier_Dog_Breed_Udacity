#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: TrucGiang
# DATE CREATED: 09.04.2024                           
# REVISED DATE: 09.04.2024
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    image_file_name_list = listdir("pet_images/")

## Print 10 of the filenames from folder pet_images/
# print("\nPrints 10 filenames from folder pet_images/")
# for idx in range(0, 10, 1):
#     print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )
#Creating an empty dictionary
    result_dict = {}
    #Creating a dictionary that contains a List as the value.
    # image_file_name_list = ["Basenji_00963.jpg","Basenji_00974.jpg","Poodle_07927.jpg","Rabbit_002.jpg"]
    ## Giang: Create a list contain the animal type from image_file_name_list
    type_of_animal = ""
    list_animal_type = []
    for x in image_file_name_list:
        type_of_animal = x.lower().replace("_"," ")
        inx = type_of_animal.rfind(" ")
        type_of_animal = type_of_animal[:inx]
        # if type_of_animal not in list_animal_type:
        list_animal_type.append(type_of_animal)
        # else:
        #     print("Duplicate the type: ",type_of_animal)
    print("List of animals type: ",list_animal_type)
    #Determines the number of items in a dictionary
    len_list_dict = len(image_file_name_list)
    #Adds key-value pairs to the dictionary if the key doesn't already exist in the dictionary
    for x in range(len_list_dict):
        # print(image_file_name_list[x])
        result_dict[image_file_name_list[x]] = [list_animal_type[x]]
        print("Key: ",x," value: ", [list_animal_type[x]])
    return(result_dict)
        # else:
        #     result_dict[image_file_name_list[x]] = image_file_name_list[x]
    
# get_pet_labels("D:\\Udacity\\Project1\\pet_images")
