
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
x=0
n=[]

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while(x<=7):
    x=x+1
    url=input("enter URL:")
    html = urllib.request.urlopen( url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


    tags = soup('a')

    for i in range(len(tags)):
        
   
        if i==17:
      
          n=tags[i]
          n=n.get('href',None)
         
          print(n)

      

 
      
      
     
      
        
     
      
        

        
        
    

    
    
        
    
    
    
    
    

    
    

    
