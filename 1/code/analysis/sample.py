# initialize sampling for sample,system/controlDict

path0 = '../sim/'

sets = path0 + 'sets.txt'
sample = path0 + 'system/sample'
control = path0 + 'system/controlDict'
special = '<setsFromSample--AutoReplace>'

with open(sets, 'r') as file:
    setval = file.read()
with open(sample, 'r') as file:
    sapval = file.read().replace(special, setval)
# with open(control, 'r') as file:
#     crlval = file.read().replace(special, setval)

with open(sample, 'w') as file:
    file.write(sapval)
# with open(control, 'w') as file:
#     file.write(crlval)
