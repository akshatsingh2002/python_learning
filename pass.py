j=int(0)
while j<3:
  c1 = c2 = c3 = c4 = int(0)
  name = input("enter the password ")
  l = int(len(name))
  if l <=int(4):
     print('password too short')
     j=j+1
     continue
  else:
  
   for i in range(l):
    if ord(name[i])>=65 and ord(name[i])<=90 :
        c1=1
  #       break
  # for i in range(l):
    if ord(name[i])>=97 and ord(name[i])<=122 :
        c2=1
  #       break
  # for i in range(l):
    if ord(name[i])>=48 and ord(name[i])<=57 :
        c3=1
  #       break
  # for i in range(l):
    if ord(name[i])>=33 and ord(name[i])<=47 :
        c4=1
        # break
  if c1==c2==c3==c4==1:
     print('password created')
     break
  else:
        j=j+1
        continue