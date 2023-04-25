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
val1 = input("Enter the first value")
val1 = int(val1)
val2 = input("Enter the second value")
val2 = int(val2)
num = max(val2,val1)
con = 0
for i in range(2,num//2+1):
    if(val1%i==0 and val2%i==0 ):
        con = 1
        break
        
if(con == 0):
    print(val1,val2,"Are co primes")
else:
    print(val1,val2,"Are not co primes")