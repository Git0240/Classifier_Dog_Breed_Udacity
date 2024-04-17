#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:TrucGiang
# DATE CREATED:       10.04.2024                           
# REVISED DATE:         16.04.2024

def calculates_results_stats(results_dic):
    results_of_dic = dict()
    
    results_of_dic['n_dogs_img'] = 0
    results_of_dic['n_match'] = 0
    results_of_dic['n_correct_dogs'] = 0
    results_of_dic['n_correct_notdogs'] = 0
    results_of_dic['n_correct_breed'] = 0       
    
    for key_rs in results_dic:
        if results_dic[key_rs][2] == 1:
            results_of_dic['n_match'] += 1
        if results_dic[key_rs][3] == 1 and results_dic[key_rs][2] == 1:
            results_of_dic['n_correct_breed'] += 1
        if results_dic[key_rs][3] == 1:
            results_of_dic['n_dogs_img'] += 1
            if results_dic[key_rs][4] == 1:
                results_of_dic['n_correct_dogs'] += 1
        else:
            if results_dic[key_rs][4] == 0:
                results_of_dic['n_correct_notdogs'] += 1
        
    results_of_dic['n_images'] = len(results_dic)
    results_of_dic['n_notdogs_img'] = (results_of_dic['n_images'] - results_of_dic['n_dogs_img']) 
    results_of_dic['pct_match'] = (results_of_dic['n_match']/results_of_dic['n_images'])*100
    if results_of_dic['n_dogs_img'] > 0:
        results_of_dic['pct_correct_dogs'] = (results_of_dic['n_correct_dogs']/results_of_dic['n_dogs_img'])*100
    else:
        results_of_dic['pct_correct_dogs'] = 0
        
    if results_of_dic['n_dogs_img'] > 0:
        results_of_dic['pct_correct_breed'] = (results_of_dic['n_correct_breed']/results_of_dic['n_dogs_img'])*100
    else:
        results_of_dic['pct_correct_breed'] = 0
 
    if results_of_dic['n_notdogs_img'] > 0:
        results_of_dic['pct_correct_notdogs'] = (results_of_dic['n_correct_notdogs'] /
                                                results_of_dic['n_notdogs_img'])*100.0
    else:
        results_of_dic['pct_correct_notdogs'] = 0
    return results_of_dic;

