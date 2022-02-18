# Parameters for this Run  
- Make sure to note these, please!

This are the parameters for "Description of the flow for Re = 10".

## Features:  
- U = 1 m/s  
- L = 0.1 m  
- ν = μ/ρ = 0.01 m2/s, giving a Reynolds number Re = UL/ν = 10.  
- blocks: (40 40 1)
- deltaT 0.0025  
- writeInterval 40  

## Notable Changes from Example:
-  4x the number of blocks to increase resolution.  
-  halved deltaT (to account for the increased blocks)   
-  doubled writeInterval (to account for the increased blocks)  
