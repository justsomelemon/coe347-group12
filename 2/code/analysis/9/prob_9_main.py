''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: prob_9_main.py                                      
 Description: This python module serves as the main program for
 the post-processing of the results obtained from part 9 of the second 
 OF assignment. '''            

# Import modules                                                 

import numpy as np
import math
from matplotlib import pyplot as plt
import get_input_data as gid
import get_radial_vel as grv
import get_tangential_vel as gtv
import get_rate_strain_tensor as grst

''' Part 1: Read in CSV files of velocity field solutions and associated coordinate 
positions into 2D numpy arrays '''


''' Read in CSV files of velocity field samples and positional coordinates for mesh configuration 
1 into a 2D numpy array '''

array_run_1_angle_pi4, array_run_1_angle_pi2, array_run_1_angle_3pi4 = \
    gid.get_input_data("Simulation_Data/run_20_1/cylnormal_pi4_U.xy", "Simulation_Data/run_20_1/cylnormal_pi2_U.xy", "Simulation_Data/run_20_1/cylnormal_3pi4_U.xy")


''' Read in CSV files of velocity field samples and positional coordinates for mesh configuration 
2 into a 2D numpy array '''

array_run_2_angle_pi4, array_run_2_angle_pi2, array_run_2_angle_3pi4 = \
    gid.get_input_data("Simulation_Data/run_20_2/cylnormal_pi4_U.xy", "Simulation_Data/run_20_2/cylnormal_pi2_U.xy", "Simulation_Data/run_20_2/cylnormal_3pi4_U.xy")


''' Read in CSV files of velocity field samples and positional coordinates for mesh configuration 
3 into a 2D numpy array '''

array_run_3_angle_pi4, array_run_3_angle_pi2, array_run_3_angle_3pi4 = \
    gid.get_input_data("Simulation_Data/run_20_3/cylnormal_pi4_U.xy", "Simulation_Data/run_20_3/cylnormal_pi2_U.xy", "Simulation_Data/run_20_3/cylnormal_3pi4_U.xy")


''' Read in CSV files of velocity field samples and positional coordinates for mesh configuration 
14into a 2D numpy array '''

array_run_4_angle_pi4, array_run_4_angle_pi2, array_run_4_angle_3pi4 = \
    gid.get_input_data("Simulation_Data/run_20_4/cylnormal_pi4_U.xy", "Simulation_Data/run_20_4/cylnormal_pi2_U.xy", "Simulation_Data/run_20_4/cylnormal_3pi4_U.xy")



'''Part 2: Evaluate radial and tangential components of velocity 
along sampling segement as function of distance "s" from the cylinder's wall '''                                                

theta_vec = [np.pi/4,np.pi/2, 3*np.pi/4] # Angles for velocity measurement (CCW from positive horizontal axis)                       


# Evaluate and return radial velocity components for simulation 1

u_r_run_1_angle_pi4, s_run_1_angle_pi4 = grv.get_radial_vel(array_run_1_angle_pi4, theta_vec[0])
u_r_run_1_angle_pi2, s_run_1_angle_pi2 = grv.get_radial_vel(array_run_1_angle_pi2, theta_vec[1])
u_r_run_1_angle_3pi4, s_run_1_angle_3pi4 = grv.get_radial_vel(array_run_1_angle_3pi4, theta_vec[2])

# Evaluate and return radial velocity components for simulation 2

u_r_run_2_angle_pi4, s_run_2_angle_pi4 = grv.get_radial_vel(array_run_2_angle_pi4, theta_vec[0])
u_r_run_2_angle_pi2, s_run_2_angle_pi2 = grv.get_radial_vel(array_run_2_angle_pi2, theta_vec[1])
u_r_run_2_angle_3pi4, s_run_2_angle_3pi4 = grv.get_radial_vel(array_run_2_angle_3pi4, theta_vec[2])

# Evaluate and return radial velocity components for simulation 3

u_r_run_3_angle_pi4, s_run_3_angle_pi4 = grv.get_radial_vel(array_run_3_angle_pi4, theta_vec[0])
u_r_run_3_angle_pi2, s_run_3_angle_pi2 = grv.get_radial_vel(array_run_3_angle_pi2, theta_vec[1])
u_r_run_3_angle_3pi4, s_run_3_angle_3pi4 = grv.get_radial_vel(array_run_3_angle_3pi4, theta_vec[2])

# Evaluate and return radial velocity components for simulation 4

u_r_run_4_angle_pi4, s_run_4_angle_pi4 = grv.get_radial_vel(array_run_4_angle_pi4, theta_vec[0])
u_r_run_4_angle_pi2, s_run_4_angle_pi2 = grv.get_radial_vel(array_run_4_angle_pi2, theta_vec[1])
u_r_run_4_angle_3pi4, s_run_4_angle_3pi4 = grv.get_radial_vel(array_run_4_angle_3pi4, theta_vec[2])


# Evaluate and return tangential velocity components for simulation 1

u_theta_run_1_angle_pi4 = gtv.get_tangential_vel(array_run_1_angle_pi4, theta_vec[0])
u_theta_run_1_angle_pi2 = gtv.get_tangential_vel(array_run_1_angle_pi2, theta_vec[1])
u_theta_run_1_angle_3pi4 = gtv.get_tangential_vel(array_run_1_angle_3pi4, theta_vec[2])

# Evaluate and return tangential velocity components for simulation 2

u_theta_run_2_angle_pi4 = gtv.get_tangential_vel(array_run_2_angle_pi4, theta_vec[0])
u_theta_run_2_angle_pi2 = gtv.get_tangential_vel(array_run_2_angle_pi2, theta_vec[1])
u_theta_run_2_angle_3pi4 = gtv.get_tangential_vel(array_run_2_angle_3pi4, theta_vec[2])

# Evaluate and return tangential velocity components for simulation 3

u_theta_run_3_angle_pi4 = gtv.get_tangential_vel(array_run_3_angle_pi4, theta_vec[0])
u_theta_run_3_angle_pi2 = gtv.get_tangential_vel(array_run_3_angle_pi2, theta_vec[1])
u_theta_run_3_angle_3pi4 = gtv.get_tangential_vel(array_run_3_angle_3pi4, theta_vec[2])

# Evaluate and return tangential velocity components for simulation 4

u_theta_run_4_angle_pi4 = gtv.get_tangential_vel(array_run_4_angle_pi4, theta_vec[0])
u_theta_run_4_angle_pi2 = gtv.get_tangential_vel(array_run_4_angle_pi2, theta_vec[1])
u_theta_run_4_angle_3pi4 = gtv.get_tangential_vel(array_run_4_angle_3pi4, theta_vec[2])

''' Generation of Plots Depicting Radial and Tangential Velocity as Function of "s" '''


# Simulation 1: Theta = pi/4

plt.plot(s_run_1_angle_pi4, u_r_run_1_angle_pi4, linestyle = '-')
plt.plot(s_run_1_angle_pi4, u_theta_run_1_angle_pi4, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 1 with Theta = pi/4", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_1_pi4.jpg", dpi = 600)
plt.show()


# Simulation 1: Theta = pi/2

plt.plot(s_run_1_angle_pi2, u_r_run_1_angle_pi2, linestyle = '-')
plt.plot(s_run_1_angle_pi2, u_theta_run_1_angle_pi2, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 1 with Theta = pi/2", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_1_pi2.jpg", dpi = 600)
plt.show()


# Simulation 1: Theta = 3pi/4

plt.plot(s_run_1_angle_3pi4, u_r_run_1_angle_3pi4, linestyle = '-')
plt.plot(s_run_1_angle_3pi4, u_theta_run_1_angle_3pi4, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 1 with Theta = 3pi/4", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_1_3pi4.jpg", dpi = 600)
plt.show()


# Simulation 2: Theta = pi/4

plt.plot(s_run_2_angle_pi4, u_r_run_2_angle_pi4, linestyle = '-')
plt.plot(s_run_2_angle_pi4, u_theta_run_2_angle_pi4, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 2 with Theta = pi/4", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_2_pi4.jpg", dpi = 600)
plt.show()


# Simulation 2: Theta = pi/2

plt.plot(s_run_2_angle_pi2, u_r_run_2_angle_pi2, linestyle = '-')
plt.plot(s_run_2_angle_pi2, u_theta_run_2_angle_pi2, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simluation 2 with Theta = pi/2", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_2_pi2.jpg", dpi = 600)
plt.show()


# Simulation 2: Theta = 3pi/4

plt.plot(s_run_2_angle_3pi4, u_r_run_2_angle_3pi4, linestyle = '-')
plt.plot(s_run_2_angle_3pi4, u_theta_run_2_angle_3pi4, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 2 with Theta = 3pi/4", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_2_3pi4.jpg", dpi = 600)
plt.show()

# Simulation 3: Theta = pi/4

plt.plot(s_run_3_angle_pi4, u_r_run_3_angle_pi4, linestyle = '-')
plt.plot(s_run_3_angle_pi4, u_theta_run_3_angle_pi4, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 3 with Theta = pi/4", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_3_pi4.jpg", dpi = 600)
plt.show()


# Simulation 3: Theta = pi/2

plt.plot(s_run_3_angle_pi2, u_r_run_3_angle_pi2, linestyle = '-')
plt.plot(s_run_3_angle_pi2, u_theta_run_3_angle_pi2, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 3 with Theta = pi/2", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_3_pi2.jpg", dpi = 600)
plt.show()


# Simulation 3: Theta = 3pi/4

plt.plot(s_run_3_angle_3pi4, u_r_run_3_angle_3pi4, linestyle = '-')
plt.plot(s_run_3_angle_3pi4, u_theta_run_3_angle_3pi4, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 3 with Theta = 3pi/4", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_3_p3i4.jpg", dpi = 600)
plt.show()


# Simulation 4: Theta = pi/4

plt.plot(s_run_4_angle_pi4, u_r_run_4_angle_pi4, linestyle = '-')
plt.plot(s_run_4_angle_pi4, u_theta_run_4_angle_pi4, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 4 with Theta = pi/4", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_4_pi4.jpg", dpi = 600)
plt.show()


# Simulation 4: Theta = pi/2

plt.plot(s_run_4_angle_pi2, u_r_run_4_angle_pi2, linestyle = '-')
plt.plot(s_run_4_angle_pi2, u_theta_run_4_angle_pi2, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 4 with Theta = pi/2", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_4_pi2.jpg", dpi = 600)
plt.show()


# Simulation 4: Theta = 3pi/4

plt.plot(s_run_4_angle_3pi4, u_r_run_4_angle_3pi4, linestyle = '-')
plt.plot(s_run_4_angle_3pi4, u_theta_run_4_angle_3pi4, linestyle = '-.')
plt.xlabel("Distance 's' from Cylinder Wall")
plt.ylabel("Velocity")
plt.title("Tangential and Radial Velocity vs Distance 's' for Simulation 4 with Theta = 3pi/4", wrap = True)
plt.legend(['Radial Velocity', 'Tangential Velocity'])
plt.savefig("sim_4_3pi4.jpg", dpi = 600)
plt.show()




''' Part 3: Evaluation of Rate of Strain Tensor at Wall  '''    

# Simulation 1:

e_rr_sim_1_theta_pi4, e_rtheta_sim_1_pi4 = grst.get_rate_strain_tensor(u_r_run_1_angle_pi4, u_theta_run_1_angle_pi4, s_run_1_angle_pi4)
e_rr_sim_1_theta_pi2, e_rtheta_sim_1_pi2 = grst.get_rate_strain_tensor(u_r_run_1_angle_pi2, u_theta_run_1_angle_pi2, s_run_1_angle_pi2)
e_rr_sim_1_theta_3pi4, e_rtheta_sim_1_3pi4 = grst.get_rate_strain_tensor(u_r_run_1_angle_3pi4, u_theta_run_1_angle_3pi4, s_run_1_angle_3pi4)

# Simulation 2: 
    
e_rr_sim_2_theta_pi4, e_rtheta_sim_2_pi4  = grst.get_rate_strain_tensor(u_r_run_2_angle_pi4, u_theta_run_2_angle_pi4, s_run_2_angle_pi4)
e_rr_sim_2_theta_pi2,  e_rtheta_sim_2_pi2  = grst.get_rate_strain_tensor(u_r_run_2_angle_pi2, u_theta_run_2_angle_pi2, s_run_2_angle_pi2)
e_rr_sim_2_theta_3pi4,  e_rtheta_sim_2_3pi4  = grst.get_rate_strain_tensor(u_r_run_2_angle_3pi4, u_theta_run_2_angle_3pi4, s_run_2_angle_3pi4)

# Simulation 3: 

e_rr_sim_3_theta_pi4,  e_rtheta_sim_3_pi4  = grst.get_rate_strain_tensor(u_r_run_3_angle_pi4, u_theta_run_3_angle_pi4, s_run_3_angle_pi4)
e_rr_sim_3_theta_pi2,  e_rtheta_sim_3_pi2  = grst.get_rate_strain_tensor(u_r_run_3_angle_pi2, u_theta_run_3_angle_pi2, s_run_3_angle_pi2)
e_rr_sim_3_theta_3pi4,  e_rtheta_sim_3_3pi4  = grst.get_rate_strain_tensor(u_r_run_3_angle_3pi4, u_theta_run_3_angle_3pi4, s_run_3_angle_3pi4)

# Simulation 4: 

e_rr_sim_4_theta_pi4,  e_rtheta_sim_4_pi4  = grst.get_rate_strain_tensor(u_r_run_4_angle_pi4, u_theta_run_4_angle_pi4, s_run_4_angle_pi4)
e_rr_sim_4_theta_pi2,  e_rtheta_sim_4_pi2  = grst.get_rate_strain_tensor(u_r_run_4_angle_pi2, u_theta_run_4_angle_pi2, s_run_4_angle_pi2)
e_rr_sim_4_theta_3pi4,  e_rtheta_sim_4_3pi4  = grst.get_rate_strain_tensor(u_r_run_4_angle_3pi4, u_theta_run_4_angle_3pi4, s_run_4_angle_3pi4)
      

''' Part 4: Generation of Plots Depicting Rate of Strain Tensors as function of "1/delta" '''

# Theta = pi/4 

delta_1 = s_run_1_angle_pi4[0]
delta_2 = s_run_1_angle_pi4[1]
size_meas_1 = 1 / np.sqrt(delta_1 * delta_2)

delta_1 = s_run_2_angle_pi4[0]
delta_2 = s_run_2_angle_pi4[1]
size_meas_2 = 1 / np.sqrt(delta_1 * delta_2)

delta_1 = s_run_3_angle_pi4[0]
delta_2 = s_run_3_angle_pi4[1]
size_meas_3 = 1 / np.sqrt(delta_1 * delta_2)

delta_1 = s_run_4_angle_pi4[0]
delta_2 = s_run_4_angle_pi4[1]
size_meas_4 = 1 / np.sqrt(delta_1 * delta_2)

size_meas_pi4 = [size_meas_1, size_meas_2, size_meas_3, size_meas_4]
e_rr_pi4 = [e_rr_sim_1_theta_pi4, e_rr_sim_2_theta_pi4, e_rr_sim_3_theta_pi4, e_rr_sim_4_theta_pi4]
e_rtheta_pi4 = [e_rtheta_sim_1_pi4, e_rtheta_sim_2_pi4, e_rtheta_sim_3_pi4, e_rtheta_sim_4_pi4]

plt.plot(size_meas_pi4, e_rr_pi4, linestyle = '-')
plt.plot(size_meas_pi4, e_rtheta_pi4, linestyle = '-')
plt.xlabel("Linear Size of Mesh Measurement (1/delta)")
plt.ylabel("Rate of Strain Tensor")
plt.title("Rate of Strain Tensor vs Linear Size of Mesh Measurement", wrap = True)
plt.legend(['e_rr', 'e_rtheta'])
plt.savefig("rate_tensor_pi4.jpg", dpi = 600)
plt.show()

# Theta = pi/2 

delta_1 = s_run_1_angle_pi2[0]
delta_2 = s_run_1_angle_pi2[1]
size_meas_1 = 1 / np.sqrt(delta_1 * delta_2)

delta_1 = s_run_2_angle_pi2[0] 
delta_2 = s_run_2_angle_pi2[1]
size_meas_2 = 1 / np.sqrt(delta_1 * delta_2)

delta_1 = s_run_3_angle_pi2[0]
delta_2 = s_run_3_angle_pi2[1]
size_meas_3 = 1 / np.sqrt(delta_1 * delta_2)

delta_1 = s_run_4_angle_pi2[0]
delta_2 = s_run_4_angle_pi2[1]
size_meas_4 = 1 / np.sqrt(delta_1 * delta_2)

size_meas_pi2 = [size_meas_1, size_meas_2, size_meas_3, size_meas_4]
e_rr_pi2 = [e_rr_sim_1_theta_pi2, e_rr_sim_2_theta_pi2, e_rr_sim_3_theta_pi2, e_rr_sim_4_theta_pi2]
e_rtheta_pi2 = [e_rtheta_sim_1_pi2, e_rtheta_sim_2_pi2, e_rtheta_sim_3_pi2, e_rtheta_sim_4_pi2]

plt.plot(size_meas_pi4, e_rr_pi4, linestyle = '-')
plt.plot(size_meas_pi4, e_rtheta_pi4, linestyle = '-')
plt.xlabel("Linear Size of Mesh Measurement (1/delta)")
plt.ylabel("Rate of Strain Tensor")
plt.title("Rate of Strain Tensor vs Linear Size of Mesh Measurement", wrap = True)
plt.legend(['e_rr', 'e_rtheta'])
plt.savefig("rate_tensor_pi2.jpg", dpi = 600)
plt.show()

# Theta = 3pi/4 

delta_1 = s_run_1_angle_3pi4[0]
delta_2 = s_run_1_angle_3pi4[1]
size_meas_1 = 1 / np.sqrt(delta_1 * delta_2)

delta_1 = s_run_2_angle_3pi4[0]
delta_2 = s_run_2_angle_3pi4[1]
size_meas_2 = 1 / np.sqrt(delta_1 * delta_2)

delta_1 = s_run_3_angle_3pi4[0]
delta_2 = s_run_3_angle_3pi4[1]
size_meas_3 = 1 / np.sqrt(delta_1 * delta_2)

delta_1 = s_run_4_angle_3pi4[0]
delta_2 = s_run_4_angle_3pi4[1]
size_meas_4 = 1 / np.sqrt(delta_1 * delta_2)

size_meas_3pi4 = [size_meas_1, size_meas_2, size_meas_3, size_meas_4]
e_rr_3pi4 = [e_rr_sim_1_theta_3pi4, e_rr_sim_2_theta_3pi4, e_rr_sim_3_theta_3pi4, e_rr_sim_4_theta_3pi4]
e_rtheta_3pi4 = [e_rtheta_sim_1_3pi4, e_rtheta_sim_2_3pi4, e_rtheta_sim_3_3pi4, e_rtheta_sim_4_3pi4]

plt.plot(size_meas_3pi4, e_rr_3pi4, linestyle = '-')
plt.plot(size_meas_3pi4, e_rtheta_3pi4, linestyle = '-')
plt.xlabel("Linear Size of Mesh Measurement (1/delta)")
plt.ylabel("Rate of Strain Tensor")
plt.title("Rate of Strain Tensor vs Linear Size of Mesh Measurement", wrap = True)
plt.legend(['e_rr', 'e_rtheta'])
plt.savefig("rate_tensor_3pi4.jpg", dpi = 600)
plt.show()
