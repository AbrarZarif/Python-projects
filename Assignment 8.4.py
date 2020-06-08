fhandle= open('mbox-short.txt')
zaru=dict()
for line in fhandle:
    if line.startswith('From '):
        z=line.split()
        person=z[1]
        
        zaru[person]=zaru.get(person,0)+1
bigcount=None
bigword=None
for word,count in zaru.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigword=word
print(bigword,bigcount)

    
        
    
    