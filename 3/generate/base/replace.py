import os


md = "../../markdown/"
suffix = ".rmd"
sep = '/'
sep2 = "  \n"
article = f'article{suffix}'
hea = f'{md}Header{suffix}'
con = f'{md}Conclusion{suffix}'
imp = f'{md}Implementation{suffix}'
mot = f'{md}Motivation{suffix}'
articlegen = f'../article{suffix}'

with open(article,'r') as file:
    main = file.read()

with open(hea,'r') as file:
    head = file.read()

with open(con,'r') as file:
    conclude = file.read()

with open(imp,'r') as file:
    implement = file.read()

with open(mot,'r') as file:
    motivate = file.read()

nSections = len(os.listdir(os.getcwd()+sep+md)) - 4
print("{} Sections in Article...".format(nSections))

maincontent=[]
for i in range(nSections):
    with open(md+sep+str(i+1)+suffix,'r') as file:
        maincontent.append(file.read())


content = motivate + sep2 + implement + sep2 + sep2.join(maincontent) + sep2 + conclude
# print("Content: {}".format(content))

with open(articlegen,'w') as file:
    file.write(main.replace("{HEADER-REPLACE}",head).replace("{CONTENT-REPLACE}",content))