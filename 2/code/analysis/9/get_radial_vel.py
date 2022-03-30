''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: get_radial_vel.py                                      
 Description: This python module is used to evaluate the distance the grid points
 along the sampling segment are displaced from the cylinder wall for a particular
 angular displacement, "theta", and, given horizontal and vertical velocity 
 components at these locations, the radial velocity components are evaluated.''' 

# Import modules                                                 

import numpy as np
import math


# Define formula for evaluating radial component of velocity using trigometry


def get_radial_vel(input_array, theta):

    
    x = np.transpose(input_array[:,0]) # Extract horizontal position components
    y = np.transpose(input_array[:,1]) # Extract vertical position components
    u = np.transpose(input_array[:,3]) # Extract horizontal velocity components
    v = np.transpose(input_array[:,4]) # Extract vertical velocity components

    u_r = np.transpose(np.zeros(len(input_array))) # Initialize vector to store radial velocity
    s = np.transpose(np.zeros(len(input_array))) # Initialize vector to store distance "s"
    
    s_baseline = np.sqrt((math.pow(x[0],2)) + math.pow(y[0],2)) # Zero out the distance "s"
    
    ''' Iterate through the number of grid points along sampling segment and 
    evaluate sampling segment distance from cylinder wall and associated 
    radial velocity '''
    
    for i in range(0, len(s)): 
        
        if i == 0:
            
            s[i] = 0
            
        else: 
            
            s[i] = np.sqrt((math.pow(x[i],2)) + math.pow(y[i], 2)) - s_baseline 
            
            u_r[i] = (u[i] * np.cos(theta)) + (v[i] * np.sin(theta))
                                          
    return u_r, s                                                                          
        


