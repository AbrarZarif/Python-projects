fhandle= open('mbox-short.txt')
zaru=dict()
shesh=dict()
import re #re maybe a library i don't know
for line in fhandle:
    if line.startswith('From '):
        z=line.split()
        person=z[5]
        x=re.split(":",person) #first you need what u want to split and then the list u wanna split
        y=x[0]
        zaru[y]= zaru.get(y,0)+1
shesh=sorted((k, v) for (k,v) in  zaru.items())

for (k,v)in shesh:
    print(k,v) 
    
    


        
        

        
