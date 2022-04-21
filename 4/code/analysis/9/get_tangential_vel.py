''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: get_tangential_vel.py                                      
 Description: This python module is used to evaluate the tangential velocity 
 components of the flow field for a particular simulation and known angular displacement
"theta". '''            

# Import modules                                                 

import numpy as np


# Define formula for evaluating tangential component of velocity using trigonometry

def get_tangential_vel(input_array, theta):
    
    u = np.transpose(input_array[:,3]) # Extract horizontal velocity components
    v = np.transpose(input_array[:,4]) # Extract vertical velocity components

    u_theta = np.transpose(np.zeros(len(input_array))) # Initialize vector to store radial velocity
    
    ''' Iterate through the number of grid points along sampling segment and 
    evaluate sampling segment distance from cylinder wall and associated 
    radial velocity '''
    
    for i in range(0, len(u)): 
            
        u_theta[i] = (u[i] * np.sin(theta)) + (v[i] * np.cos(theta))
                                          
    return u_theta                                                                          
        
        

