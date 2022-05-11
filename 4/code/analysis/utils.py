import os
cwd = os.getcwd()
datapath = cwd+'/../data/'
plotdir = cwd+'/../../plots/'


def makedir(run): return os.system("mkdir -p "+plotdir+run+"/ ")


def filename(run): return datapath+run+'/_.foam'


def plotpath(run, number): return plotdir+run+"/"+number+'.jpg'


def plotpath2(run, folder, name):
    os.makedirs(plotdir+run+"/"+folder, exist_ok=True)
    return plotdir+run+"/"+folder+"/"+name+'.jpg'
