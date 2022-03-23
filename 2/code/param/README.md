# parameters for each run

## Note

- All major setting changes are listed in settings.json. Will look like the following example:
```
[
    {
        "id" : "run_0",
        "endTime": 0.5,
        "deltaT": 0.005,
        "writeInterval": 0.1,
    },

    {
        "id" : "run_1",
        "Re" : 110,
        "endTime": 0.5,
        "deltaT": 0.005,
        "writeInterval": 0.1,
    },
]
```
- A python script will iterate through each of these files and create individual run parameter folders.
- Individual overrides can be created by simply placing the corresponding file in the appropriate `run_<#>` folder.

## Supporting parameters:

- We currently support setting any of the following parameters through settings.json. It is suggested to <i>only</i> set the Reynolds number, as everything else has appropriate defaults enabled.
```
'Re',
'f', 'R', 'R2', 'H', 'F', 'W', 'K',
'nu','endTime','writeControl','writeInterval','deltaT',
'probeLocations','recirculation','cylwall,
'cylnormal_pi4','cylnormal_pi2','cylnormal_3pi4',
'cores'
```

## Dictionary of Terms:

# Pi parameters:  

Self-explanatory:

- Re : Reynolds Number, ex: `10`

# Key parameters:

Special mesh dimension parameters

- f : blockMeshFactor (decreases cell dimensions in each direction by this factor), set by default : `int(max(10, pi.Re/3))`
- R : cylinder radius, default: `1/2`
- R2 : ring block outer radius, default: `3/2`
- H : height as in Prof.'s example, default: `4`
- F : forward distance as in Prof.'s example, default: `4`
- W : wake (backward) distance as in Prof.'s example, default: `4 + pi.Re*(1/15)`
- K : +/- distance in Z-axis --- mostly irrelevant for Re in this project, default: `4`

# Param parameters:

Other parameters (typically generated from the above). Most are self explanatory, but some are mentioned here as well.

- 'nu','endTime','writeControl','writeInterval','deltaT' : same as in the OpenFoam files, defaults generated from the above numbers so as to not overwhelm Courant #. The writeInterval is 0.1s by default.

- 'probeLocations','recirculation','cylwall, 'cylnormal_pi4','cylnormal_pi2','cylnormal_3pi4' : OpenFoam slicing parameters that will automatically overwrite the blank spots in `template/system/probes` and `template/system/singleGraph`. Should not be edited directly, due to the size of these values. (This still needs work...)
