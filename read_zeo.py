import re


doc='cumil.resex'
file=open(doc,'r')


namelist=[] #list of zeolite names
pldlist=[] #list of pore limiting diameters
lcdlist=[] #list of largest cavity diameter

for line in file:
	nm=re.split(r"[ :]", line)
	namelist.append(nm[1])
	pldlist.append(nm[15])
	lcdlist.append(nm[21])

#print(namelist)
#print(pldlist)
#print(lcdlist)

#---------------------------------------------------
# Screening for uniqueness of framework
dlist=[] #list of frameworks done
ulist=[] #list of unique frameworks
ii=len(namelist)
i=0
while(i < ii):
	name=(namelist[i].split('-'))[0]
	if name not in dlist:
		dlist.append(name)
		ulist.append([namelist[i],pldlist[i],lcdlist[i]])
	i=i+1

for i in ulist:
	print(i)
	yoyo=9



#--------------------------------------------------
#screened for certain pore size
slist=[] # name pld lcd

mind=2.9
maxd=3.3

ii=len(ulist)
i=0
while( i < ii):
	pld=float((ulist[i])[1])
	if mind <= pld <= maxd:
		slist.append(ulist[i])
	i=i+1

for i in slist:
	print(i)
	yoyo=0



'''
#---------------------------------------------------
# Basically all data read in from file.
alllist=[]# list of all name,pld,lcd

ii=len(namelist)
i=0
while( i < ii):
	alllist.append([namelist[i],pldlist[i],lcdlist[i]])
	i=i+1
for i in alllist:
	print(i)
'''
'''
#-----------------------------------------------
#screened for certain pore size
slist=[] # name pld lcd

mind=2.9
maxd=3.3

ii=len(pldlist)
i=0
while( i < ii):
	pld=float(pldlist[i])
	if mind <= pld <= maxd:
		slist.append([namelist[i],pldlist[i],lcdlist[i]])
	i=i+1

for i in slist:
	print(i)
	yoyo=0
'''
		
	