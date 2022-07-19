from posixpath import split


lst =[]
lst2=[]
i=0
while i<1:
    imp = input("enter the method")
    lst=split(imp)
    met=lst[0]
    value=lst[1]
    
    if(imp=="push"):
        lst2.append(value)
    elif ( imp=="pop"):
        lst2.remove(value)
    elif (imp=="stop"):
        break
    
print(lst2)
    
    