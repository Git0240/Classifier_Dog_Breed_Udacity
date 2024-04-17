#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: TrucGiang
# DATE CREATED:        10.04.2024                         
# REVISED DATE:        10.04.2024

def adjust_results4_isadog(results_dic, dogfile):
    dogs_dic = dict()
    with open(dogfile, "r") as txtfile:
        line_in_file = txtfile.readline()
        while line_in_file != "":
            line_in_file = line_in_file.rstrip("\n")
            if line_in_file not in dogs_dic:
                dogs_dic[line_in_file] = 1
            line_in_file = txtfile.readline()
    for key_rs in results_dic:
        if results_dic[key_rs][0] in dogs_dic:
            if results_dic[key_rs][1] in dogs_dic:
                results_dic[key_rs].extend((1, 1))
            else:
                results_dic[key_rs].extend((1, 0))
        else:
            if results_dic[key_rs][1] in dogs_dic:
                results_dic[key_rs].extend((0, 1))
            else:
                results_dic[key_rs].extend((0, 0))
    None
