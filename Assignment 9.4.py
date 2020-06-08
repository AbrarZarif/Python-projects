fhandle= open('mbox-short.txt')
zaru=dict()
for line in fhandle:
    if line.startswith('From '):
        z=line.split()
        zaru[z[1]]=zaru.get(z[1],0)+1
bigcount=None
bigword=None
for time,count in zaru.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=time
print(bigword,bigcount)

    
        
    
    