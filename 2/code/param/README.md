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
'Re','f', 'R', 'H', 'F', 'W',
'nu','endTime','writeControl','writeInterval',
'deltaT','probeLocations','recirculation','cylwall,
'cylnormal_pi4','cylnormal_pi2','cylnormal_3pi4',
'cores'
```