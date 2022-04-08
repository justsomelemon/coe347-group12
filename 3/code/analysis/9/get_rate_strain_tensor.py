''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: get_rate_strain_tensor.py                                      
 Description: This python module evaluates the rate of strain tensor at the wall
 for each angular displacement, theta, and simulation run in problem 9.''' 

# Import modules                                                 

import numpy as np

def get_rate_strain_tensor(u_r, u_theta, s):

    ''' Using one-sided first order Finite Difference App. for "e_rr" '''
    
    s_step = s[1] - s[0] # Define grid spacing along "s" path 
    
    e_rr = ((-11 * u_r[0]) + (18 * u_r[1]) - (9 * u_r[2]) + (2 * u_r[3])) / (6 * s_step)
    
    
    ''' Using one-sided first order Finite Difference App. for "e_rtheta" '''
    
    r = np.transpose(np.array(np.zeros(4)))
    
    for i in range(0, 4):
        
        r[i] = 0.5 + s[i] # Radial position "r" is incremented by "s" for each grid position
    
    
    e_rtheta = (r[0] /  2) * ((-11 * u_theta[0]/r[0]) + (18 * u_theta[1]/r[1]) - (9 * u_theta[2]/r[2]) + (2 * u_theta[3]/r[3])) / (6 * s_step)
    
    
    
    

    return e_rr, e_rtheta