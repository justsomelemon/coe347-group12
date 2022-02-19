# Parameters for this Run  
- Make sure to note these, please!

This are the parameters for "Description of the flow for Re = 10" (#3).

## Features:  
- U = 1 m/s  
- L = 0.1 m  
- ν = μ/ρ = 0.01 m2/s, giving a Reynolds number Re = UL/ν = 10.  
- *blocks: (80 80 1)*
- *deltaT 0.00125*  
- *writeInterval 80*  

## Notable Changes from Example:
-  16x the number of blocks to increase resolution.  
-  1/4th deltaT (to account for the increased blocks)   
-  4x writeInterval (to account for the increased blocks)  
-  Added sampling line in sets.txt
