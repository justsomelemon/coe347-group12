''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: get_input_data.py                                      
 Description: This python module is used to read in velocity field, pressure, fluid density, 
 and temperature solutions and associated computational domain coordinate positions for part 6
 of the OF 3 assignment. These properties will be read in as a CSV file and converted to 2D numpy arrays for further manipulation '''

# Import modules                                                 

import numpy as np


def get_input_data(filename_1, filename_2, filename_3, filename_4, filename_5, filename_6, filename_7, filename_8):
    
    ''' Read in CSV files of velocity field, pressure, fluid density, and temperature solutions
    for a particular mesh configuration'''
    
    CSV_object_1 = open(filename_1) 
    CSV_object_2 = open(filename_2) 
    CSV_object_3 = open(filename_3)
    CSV_object_4 = open(filename_4) 
    CSV_object_5 = open(filename_5) 
    CSV_object_6 = open(filename_6)
    CSV_object_7 = open(filename_7) 
    CSV_object_8 = open(filename_8) 
    
    ''' Read object file of solutions for mesh configuration 
    into a 2D numpy array '''

    array_input_1 = np.loadtxt(CSV_object_1)
    array_input_2 = np.loadtxt(CSV_object_2)
    array_input_3 = np.loadtxt(CSV_object_3)
    array_input_4 = np.loadtxt(CSV_object_4)
    array_input_5 = np.loadtxt(CSV_object_5)
    array_input_6 = np.loadtxt(CSV_object_6)
    array_input_7 = np.loadtxt(CSV_object_7)
    array_input_8 = np.loadtxt(CSV_object_8)
    
    
    return array_input_1, array_input_2, array_input_3, array_input_4, array_input_5, array_input_6, array_input_7, array_input_8 
