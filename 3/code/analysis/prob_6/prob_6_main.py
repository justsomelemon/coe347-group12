''' Property of: Justin Campbell # UT eID: jsc4348                 
 File Name: prob_6_main.py                                      
 Description: This python module serves as the main program for
 the post-processing of the results obtained from part 6 of the third
 OF assignment. '''            

# Import modules                                                 

import numpy as np
from matplotlib import pyplot as plt
import get_input_data as gid


''' Part 1: Read in CSV files of velocity field, pressure field, fluid density field, and
temperature field solutions and associated distances into 2D numpy arrays '''


''' Read in CSV files of properties for simulation 
1 with spatial resolution of 0.04 into a 2D numpy array '''

A_p_rho_T_1, A_U_1, B_p_rho_T_1, B_U_1, C_p_rho_T_1, C_U_1, D_p_rho_T_1, D_U_1 = \
    gid.get_input_data("run_5_64/postProcessing/A_p_rho_T.xy", "run_5_64/postProcessing/A_U.xy", "run_5_64/postProcessing/B_p_rho_T.xy", "run_5_64/postProcessing/B_U.xy", "run_5_64/postProcessing/C_p_rho_T.xy", "run_5_64/postProcessing/C_U.xy", "run_5_64/postProcessing/D_p_rho_T.xy", "run_5_64/postProcessing/D_U.xy")

''' Read in CSV files of properties for simulation 2
2 with spatial resoluton of 0.02 into a 2D numpy array '''


A_p_rho_T_2, A_U_2, B_p_rho_T_2, B_U_2, C_p_rho_T_2, C_U_2, D_p_rho_T_2, D_U_2 = \
    gid.get_input_data("run_10_64/postProcessing/A_p_rho_T.xy", "run_10_64/postProcessing/A_U.xy", "run_10_64/postProcessing/B_p_rho_T.xy", "run_10_64/postProcessing/B_U.xy", "run_10_64/postProcessing/C_p_rho_T.xy", "run_10_64/postProcessing/C_U.xy", "run_10_64/postProcessing/D_p_rho_T.xy", "run_10_64/postProcessing/D_U.xy")


''' Read in CSV files of properties for simulation 3
3 with spatial resolution of 0.000625 into a 2D numpy array '''

A_p_rho_T_3, A_U_3, B_p_rho_T_3, B_U_3, C_p_rho_T_3, C_U_3, D_p_rho_T_3, D_U_3 = \
    gid.get_input_data("run_32_64/postProcessing/A_p_rho_T.xy", "run_32_64/postProcessing/A_U.xy", "run_32_64/postProcessing/B_p_rho_T.xy", "run_32_64/postProcessing/B_U.xy", "run_32_64/postProcessing/C_p_rho_T.xy", "run_32_64/postProcessing/C_U.xy", "run_32_64/postProcessing/D_p_rho_T.xy", "run_32_64/postProcessing/D_U.xy")


# Extraction of density, velocity, pressure fields from input arrays 


# Mesh 1: 
       
A_p_1 = A_p_rho_T_1[:,3]
A_rho_1 = A_p_rho_T_1[:,4]
A_T_1 = A_p_rho_T_1[:,5]
A_p_rho_T_x_1 = A_p_rho_T_1[:,0]
A_U_u_1 = A_U_1[:, 3]
A_U_v_1 = A_U_1[:, 4]
A_U_x_1 = A_U_1[:, 0]
B_p_1 = B_p_rho_T_1[:,3]
B_rho_1 = B_p_rho_T_1[:,4]
B_T_1 = B_p_rho_T_1[:,5]
B_p_rho_T_y_1 = B_p_rho_T_1[:,1]
B_U_u_1 = B_U_1[:, 3]
B_U_v_1 = B_U_1[:, 4]
B_U_y_1 = B_U_1[:, 1]
C_p_1 = C_p_rho_T_1[:,3]
C_rho_1 = C_p_rho_T_1[:,4]
C_T_1 = C_p_rho_T_1[:,5]
C_p_rho_T_x_1 = C_p_rho_T_1[:,0]
C_U_u_1 = C_U_1[:, 3]
C_U_v_1 = C_U_1[:, 4]
C_U_x_1 = C_U_1[:, 0]
D_p_1 = D_p_rho_T_1[:,3]
D_rho_1 = D_p_rho_T_1[:,4]
D_T_1 = D_p_rho_T_1[:,5]
D_p_rho_T_x_1 = D_p_rho_T_1[:,0]
D_U_u_1 = D_U_1[:, 3]
D_U_v_1 = D_U_1[:, 4]
D_U_x_1 = D_U_1[:, 0]

# Mesh 2: 
       
A_p_2 = A_p_rho_T_2[:,3]
A_rho_2 = A_p_rho_T_2[:,4]
A_T_2 = A_p_rho_T_2[:,5]
A_p_rho_T_x_2 = A_p_rho_T_2[:,0]
A_U_u_2 = A_U_2[:, 3]
A_U_v_2 = A_U_2[:, 4]
A_U_x_2 = A_U_2[:, 0]
B_p_2 = B_p_rho_T_2[:,3]
B_rho_2 = B_p_rho_T_2[:,4]
B_T_2 = B_p_rho_T_2[:,5]
B_p_rho_T_y_2 = B_p_rho_T_2[:,1]
B_U_u_2 = B_U_2[:, 3]
B_U_v_2 = B_U_2[:, 4]
B_U_y_2 = B_U_2[:, 1]
C_p_2 = C_p_rho_T_2[:,3]
C_rho_2 = C_p_rho_T_2[:,4]
C_T_2 = C_p_rho_T_2[:,5]
C_p_rho_T_x_2 = C_p_rho_T_2[:,0]
C_U_u_2 = C_U_2[:, 3]
C_U_v_2 = C_U_2[:, 4]
C_U_x_2 = C_U_2[:, 0]
D_p_2 = D_p_rho_T_2[:,3]
D_rho_2 = D_p_rho_T_2[:,4]
D_T_2 = D_p_rho_T_2[:,5]
D_p_rho_T_x_2 = D_p_rho_T_2[:,0]
D_U_u_2 = D_U_2[:, 3]
D_U_v_2 = D_U_2[:, 4]
D_U_x_2 = D_U_2[:, 0]

# Mesh 3: 
       
A_p_3 = A_p_rho_T_3[:,3]
A_rho_3 = A_p_rho_T_3[:,4]
A_T_3 = A_p_rho_T_3[:,5]
A_p_rho_T_x_3 = A_p_rho_T_3[:,0]
A_U_u_3 = A_U_3[:, 3]
A_U_v_3= A_U_3[:, 4]
A_U_x_3 = A_U_3[:, 0]
B_p_3 = B_p_rho_T_3[:,3]
B_rho_3 = B_p_rho_T_3[:,4]
B_T_3 = B_p_rho_T_3[:,5]
B_p_rho_T_y_3 = B_p_rho_T_3[:,1]
B_U_u_3 = B_U_3[:, 3]
B_U_v_3 = B_U_3[:, 4]
B_U_y_3 = B_U_3[:, 1]
C_p_3 = C_p_rho_T_3[:,3]
C_rho_3 = C_p_rho_T_3[:,4]
C_T_3 = C_p_rho_T_3[:,5]
C_p_rho_T_x_3 = C_p_rho_T_3[:,0]
C_U_u_3 = C_U_3[:, 3]
C_U_v_3 = C_U_3[:, 4]
C_U_x_3 = C_U_3[:, 0]
D_p_3 = D_p_rho_T_3[:,3]
D_rho_3 = D_p_rho_T_3[:,4]
D_T_3 = D_p_rho_T_3[:,5]
D_p_rho_T_x_3 = D_p_rho_T_3[:,0]
D_U_u_3 = D_U_3[:, 3]
D_U_v_3 = D_U_3[:, 4]
D_U_x_3 = D_U_3[:, 0]


''' Generation of Plots Depicting Pressure as Function of Position Across Surfaces A:D for Each Mesh Resolution" '''


# Surface A

plt.plot(A_p_rho_T_x_1, A_p_1, linestyle = '-.')
plt.plot(A_p_rho_T_x_2, A_p_2, linestyle = '-.')
plt.plot(A_p_rho_T_x_3, A_p_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Bottom Wall 'A'")
plt.ylabel("Pressure")
plt.title("Pressure vs Distance 's' Along A for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("A_p.jpg", dpi = 600)
plt.show()

# Surface B

plt.plot(B_p_rho_T_y_1, B_p_1, linestyle = '-.')
plt.plot(B_p_rho_T_y_2, B_p_2, linestyle = '-.')
plt.plot(B_p_rho_T_y_3, B_p_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Vertical Step Wall 'B'")
plt.ylabel("Pressure")
plt.title("Pressure vs Distance 's' Along B for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("B_p.jpg", dpi = 600)
plt.show()

# Surface C

plt.plot(C_p_rho_T_x_1, C_p_1, linestyle = '-.')
plt.plot(C_p_rho_T_x_2, C_p_2, linestyle = '-.')
plt.plot(C_p_rho_T_x_3, C_p_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Horizontal Step Wall 'C'")
plt.ylabel("Pressure")
plt.title("Pressure vs Distance 's' Along C for Different Resolutions")
plt.legend(['Mesh with h = 0.004', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("C_p.jpg", dpi = 600)
plt.show()

# Surface D

plt.plot(D_p_rho_T_x_1, D_p_1, linestyle = '-.')
plt.plot(D_p_rho_T_x_2, D_p_2, linestyle = '-.')
plt.plot(D_p_rho_T_x_3, D_p_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Top Horizontal Wall 'D'")
plt.ylabel("Pressure")
plt.title("Pressure vs Distance 's' Along D for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("D_p.jpg", dpi = 600)
plt.show()

''' Generation of Plots Depicting Fluid Density as Function of Position Across Surfaces A:D for Each Mesh Resolution" '''


# Surface A

plt.plot(A_p_rho_T_x_1, A_rho_1, linestyle = '-.')
plt.plot(A_p_rho_T_x_2, A_rho_2, linestyle = '-.')
plt.plot(A_p_rho_T_x_3, A_rho_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Bottom Wall 'A'")
plt.ylabel("Density")
plt.title("Density vs Distance 's' Along A for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("A_rho.jpg", dpi = 600)
plt.show()

# Surface B

plt.plot(B_p_rho_T_y_1, B_rho_1, linestyle = '-.')
plt.plot(B_p_rho_T_y_2, B_rho_2, linestyle = '-.')
plt.plot(B_p_rho_T_y_3, B_rho_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Vertical Step Wall 'B'")
plt.ylabel("Density")
plt.title("Density vs Distance 's' Along B for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("B_rho.jpg", dpi = 600)
plt.show()

# Surface C

plt.plot(C_p_rho_T_x_1, C_rho_1, linestyle = '-.')
plt.plot(C_p_rho_T_x_2, C_rho_2, linestyle = '-.')
plt.plot(C_p_rho_T_x_3, C_rho_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Horizontal Step Wall 'C'")
plt.ylabel("Density")
plt.title("Density vs Distance 's' Along C for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("C_rho.jpg", dpi = 600)
plt.show()

# Surface D

plt.plot(D_p_rho_T_x_1, D_rho_1, linestyle = '-.')
plt.plot(D_p_rho_T_x_2, D_rho_2, linestyle = '-.')
plt.plot(D_p_rho_T_x_3, D_rho_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Top Horizontal Wall 'D'")
plt.ylabel("Density")
plt.title("Density vs Distance 's' Along D for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("D_rho.jpg", dpi = 600)
plt.show()

''' Generation of Plots Depicting Temperature as Function of Position Across Surfaces A:D for Each Mesh Resolution" '''

# Surface A

plt.plot(A_p_rho_T_x_1, A_T_1, linestyle = '-.')
plt.plot(A_p_rho_T_x_2, A_T_2, linestyle = '-.')
plt.plot(A_p_rho_T_x_3, A_T_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Bottom Wall 'A'")
plt.ylabel("Temperature")
plt.title("Temperature vs Distance 's' Along A for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("A_temp.jpg", dpi = 600)
plt.show()

# Surface B

plt.plot(B_p_rho_T_y_1, B_T_1, linestyle = '-.')
plt.plot(B_p_rho_T_y_2, B_T_2, linestyle = '-.')
plt.plot(B_p_rho_T_y_3, B_T_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Vertical Step Wall 'B'")
plt.ylabel("Temperature")
plt.title("Temperature vs Distance 's' Along B for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("B_temp.jpg", dpi = 600)
plt.show()

# Surface C

plt.plot(C_p_rho_T_x_1, C_T_1, linestyle = '-.')
plt.plot(C_p_rho_T_x_2, C_T_2, linestyle = '-.')
plt.plot(C_p_rho_T_x_3, C_T_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Horizontal Step Wall 'C'")
plt.ylabel("Temperature")
plt.title("Temperature vs Distance 's' Along C for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("C_temp.jpg", dpi = 600)
plt.show()

# Surface D

plt.plot(D_p_rho_T_x_1, D_T_1, linestyle = '-.')
plt.plot(D_p_rho_T_x_2, D_T_2, linestyle = '-.')
plt.plot(D_p_rho_T_x_3, D_T_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Top Horizontal Wall 'D'")
plt.ylabel("Temperature")
plt.title("Temperature vs Distance 's' Along D for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("D_temp.jpg", dpi = 600)
plt.show()

''' Generation of Plots Depicting x-component of Velocity as Function of Position Across Surfaces A:D for Each Mesh Resolution" '''


# Surface A

plt.plot(A_U_x_1, A_U_u_1, linestyle = '-.')
plt.plot(A_U_x_2, A_U_u_2, linestyle = '-.')
plt.plot(A_U_x_3, A_U_u_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Bottom Wall 'A'")
plt.ylabel("x-component of Velocity (u)")
plt.title("x-component of Velocity vs Distance Along A for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("A_u.jpg", dpi = 600)
plt.show()

# Surface B

plt.plot(B_U_y_1, B_U_u_1, linestyle = '-.')
plt.plot(B_U_y_2, B_U_u_2, linestyle = '-.')
plt.plot(B_U_y_3, B_U_u_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Vertical Step Wall 'B'")
plt.ylabel("x-component of Velocity (u)")
plt.title("x-component of Velocity vs Distance Along B for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("B_u.jpg", dpi = 600)
plt.show()

# Surface C

plt.plot(C_U_x_1, C_U_u_1, linestyle = '-.')
plt.plot(C_U_x_2, C_U_u_2, linestyle = '-.')
plt.plot(C_U_x_3, C_U_u_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Horizontal Step Wall 'C'")
plt.ylabel("x-component of Velocity (u)")
plt.title("x-component of Velocity vs Distance Along C for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("C_u.jpg", dpi = 600)
plt.show()

# Surface D

plt.plot(D_U_x_1, D_U_u_1, linestyle = '-.')
plt.plot(D_U_x_2, D_U_u_2, linestyle = '-.')
plt.plot(D_U_x_3, D_U_u_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Upper Wall 'D'")
plt.ylabel("x-component of Velocity (u)")
plt.title("x-component of Velocity vs Distance Along D for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.000625'])
plt.savefig("D_u.jpg", dpi = 600)
plt.show()


''' Generation of Plots Depicting y-component of Velocity as Function of Position Across Surfaces A:D for Each Mesh Resolution" '''


# Surface A

plt.plot(A_U_x_1, A_U_v_1, linestyle = '-.')
plt.plot(A_U_x_2, A_U_v_2, linestyle = '-.')
plt.plot(A_U_x_3, A_U_v_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Bottom Wall 'A'")
plt.ylabel("y-component of Velocity (u)")
plt.title("y-component of Velocity vs Distance Along A for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("A_v.jpg", dpi = 600)
plt.show()

# Surface B

plt.plot(B_U_y_1, B_U_v_1, linestyle = '-.')
plt.plot(B_U_y_2, B_U_v_2, linestyle = '-.')
plt.plot(B_U_y_3, B_U_v_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Vertical Step Wall 'B'")
plt.ylabel("y-component of Velocity (u)")
plt.title("y-component of Velocity vs Distance Along B for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("B_v.jpg", dpi = 600)
plt.show()

# Surface C

plt.plot(C_U_x_1, C_U_v_1, linestyle = '-.')
plt.plot(C_U_x_2, C_U_v_2, linestyle = '-.')
plt.plot(C_U_x_3, C_U_v_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Horizontal Step Wall 'C'")
plt.ylabel("y-component of Velocity (u)")
plt.title("y-component of Velocity vs Distance Along C for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("C_v.jpg", dpi = 600)
plt.show()

# Surface D

plt.plot(D_U_x_1, D_U_v_1, linestyle = '-.')
plt.plot(D_U_x_2, D_U_v_2, linestyle = '-.')
plt.plot(D_U_x_3, D_U_v_3, linestyle = '-.')
plt.xlabel("Distance 's' Along Upper Wall 'D'")
plt.ylabel("y-component of Velocity (u)")
plt.title("y-component of Velocity vs Distance Along D for Different Resolutions")
plt.legend(['Mesh with h = 0.04', 'Mesh with h = 0.02', 'Mesh with h = 0.00625'])
plt.savefig("D_v.jpg", dpi = 600)
plt.show()