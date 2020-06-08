import urllib.request, urllib.parse, urllib.error
import json 
import ssl
q=0



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
address = input('Enter URl: ')
  

uh = urllib.request.urlopen(address, context=ctx).read()  
x=uh.decode()
y=json.loads(x)
z=y['comments']

X=z.get("count")
X=int(X)
q=q+X
print(q)
      

      
       
    

 
        