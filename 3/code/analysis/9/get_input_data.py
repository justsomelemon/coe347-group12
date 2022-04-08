''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: get_input_data.py                                      
 Description: This python module is used to read in velocity field solutions and 
 associated computational domain coordinate positions for sample segments 
 extracted normal to the cylinder wall for problem 9. These properties will be 
 read in as a CSV file and converted to 2D numpy arrays for further manipulation '''

# Import modules                                                 

import numpy as np


def get_input_data(filename_1, filename_2, filename_3):
    
    ''' Read in CSV files of velocity field samples and positional coordinates for mesh configuration 
    into an object file '''
    
    CSV_object_angle_1 = open(filename_1) # Read velocity data for theta = pi/4
    CSV_object_angle_2 = open(filename_2) # Read velocity data for theta = pi/2
    CSV_object_angle_3 = open(filename_3) # Read velocity data for theta = 3*pi/4
    
    ''' Read object file of velocity field samples and positional coordinates for mesh configuration 
    into a 2D numpy array '''

    array_input_angle_1 = np.loadtxt(CSV_object_angle_1)
    array_input_angle_2 = np.loadtxt(CSV_object_angle_2)
    array_input_angle_3 = np.loadtxt(CSV_object_angle_3)
    
    return array_input_angle_1, array_input_angle_2, array_input_angle_3



