# num = input("ENter the number to check whether it is prime our not ")
# num = int(num)
# con = 0
# for i in range(2,num//2):
#     if(num%i==0):
#         con = 1
#         break
    
    
# if(con == 0):
#     print(num," is prime")

# else:
#     print(num," is not prime")

##NUmbers are called co-primes if their hcf is only one
# val1 = input("Enter the first value")
# val1 = int(val1)
# val2 = input("Enter the second value")
# val2 = int(val2)
# num = max(val2,val1)
# con = 0
# for i in range(2,num//2+1):
#     if(val1%i==0 and val2%i==0 ):
#         con = 1
#         break
        
# if(con == 0):
#     print(val1,val2,"Are co primes")
# else:
#     print(val1,val2,"Are not co primes")


# val = input("Enter a value")
# for i in val:
#     if(ord(i)>=97 and ord(i)<=122 and i!='a' and i!='u'and i!='o'and i!='i'and i!='e'):
#         print(i)
#     elif(ord(i)>=65 and ord(i)<=90 and i!='A' and i!='E'and i!='I'and i!='O'and i!='U'):
#         print(i)

import copy
myList1 = [1,2,3,4,5]
print(id(myList1))
print(myList1)
mylist2 = copy.copy(myList1)
mylist2.append(10)
print(myList1)
print(id(mylist2))
print(mylist2)