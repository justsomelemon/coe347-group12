# OF1 Assignment

## Methodology

 - The goal is to make the project as modular as possible, to that end we have several folders for each part.  
 - All code and paper generation should be runnable from a single script. So each modification to an OpenFoam simulation should be done programmatically (make copies of input commands and replace those files via a bash/Python3 script).  
 - At any point, use proper Git commands! At the moment I am assuming we will develop directly on `main`, pulling, adding changes, committing, and pushing as necessary.  
  - So to avoid merge issues, please DO NOT push to the same folder at once!  
  - In particular, send a Slack message that you are working on a folder, and when you finish, let us know on the same chain, so that another person can make their changes.  
  - This does not apply to the `markdown/` or `pdf/` folders, as the markdown folder will consist of individual documents that need to be added to the final pdf (so async changes can be made), and the `pdf/` contains generated output, so no modifications should be made there!  
 - As this methodology can undoubtedly be improved, please email / group chat on Slack us with your ideas/concerns!  

## Folders

- code  
 - contains OpenFoam files, Python3 / paraview analysis files, and a couple of Bash scripts to run each version of the program. (Like the following...)  
```
├── analysis
├── analyze.sh
├── data
├── param
│   └── 1
│       └── README.txt
├── run.sh
└── sim
```  
- generate  
 - contains a script and R files to stitch together plots from R Markdown from `markdown/` into the `pdf/` output directory.  
 - you should NOT need to edit this file once I have created it, just run the `generate.sh` script, via `bash generate.sh -c`.  
- pdf  
 - output directory, do not edit anything here  
- plots  
 - generated plots from the simulation and analysis  
- markdown  
 - contains individual files for each section, numbered `1,2,...`. Please edit your email address into the Header.rmd file! 
# Output  
 - PDF and HTML versions are linked here.
 https://github.com/akhilsadam/coe347-group12/tree/main/1/pdf/article.pdf
 https://github.com/akhilsadam/coe347-group12/tree/main/1/pdf/article.html  

 <embed src="https://raw.githubusercontent.com/akhilsadam/coe347-group12/main/1/pdf/article.html" width=100% height=100%></embed>  

