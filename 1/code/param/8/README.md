# Parameters for this Run  
- Make sure to note these, please!

This are the parameters for "Force on the Lid".

## Features:  
- U = 1 m/s  
- L = 0.1 m  
- ν = μ/ρ = 0.00125 m2/s, giving a Reynolds number Re = UL/ν = 80.  
- blocks: (160 160 1)
- deltaT 0.000625  
- writeInterval 0.1  
- writeControl runTime   

## Notable Changes from Example:
-  Added sampling line in sets.txt for lid.
-  Doubling the length scale, since the local gradients ought to be similar!
-  Also halving timestep, since Courant number ought to be less than 1

