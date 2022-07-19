from asyncio.windows_events import NULL
from posixpath import split


lst =[]
lst2=[]
i=0
while i<1:
    imp = input("enter the method")
    lst=imp.split()
    met=lst[0]
    if(met!="stop"):
     value=lst[1]
    print(lst)
    
    if(met=="push"):
        lst2.append(value)
    elif ( met=="pop"):
       u = lst2.remove(value)
       if(u == NULL):
           print('element does not exist')
           break
    elif (met=="stop"):
        break
    
print(lst2)
    
    