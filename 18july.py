n = int(input("enter the number of inputs"))

for i in range(n):
    
  op=input()
  lst=op.split()
  l = int(len(lst))
  
  if(lst[0]=='add'):
      add = int(0)
      
      for  j in range(1,l):
          add=add+int(lst[j])
          
      print(add)
      
  if(lst[0]=='mul'):
      mul = int(1)
      
      for j in range(1,l):
          mul=mul*int(lst[j])
          
      print(mul)
      
  if(lst[0]=='sub'):
   print(int(lst[1])-int(lst[2]))
   
  if(lst[0]=='div'):
   print(int(lst[1])/int(lst[2]))
