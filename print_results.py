#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: TrucGiang 
# DATE CREATED: 10.04.2024
# REVISED DATE: 16.04.2024

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
        print('Model trained: {}'.format(model)+' \n')
        print('Amount Img: {} \n Amount Dog File: {} \n Amount not Dog File: {}'.format(results_stats_dic['n_images'], results_stats_dic['n_dogs_img'], results_stats_dic['n_notdogs_img']))
        for key_rs in results_stats_dic:
                if key_rs[0] == 'p':
                        print('{}: {}'.format(key_rs, results_stats_dic[key_rs]))
        if print_incorrect_dogs == True and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
                for key_rs in results_dic:
                        if sum(results_dic[key_rs][3:]) == 1:
                                print('Dogs: \n Image: {} \n Classifier: {}'.format(results_dic[key_rs][0], results_dic[key_rs][1]))
        if print_incorrect_breed == True and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
                for key_rs in results_dic:   
                        if sum(results_dic[key_rs][3:]) == 2 and results_dic[key_rs][2] == 0:
                                print('\nBreeds: \n Image : {} \n Classifier: {}'.format(results_dic[key_rs][0], results_dic[key_rs][1]))