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


val1 = input("Enter the first value")
val1 = int(val1)
val2 = input("Enter the second value")
val2 = int(val2)
num = max(val2,val1)
con = 0
for i in range(2,num//2+1):
    if(val1%i==0 and val2%i==0 and con<=1):
        con = con + 1
        
if(con == 1):
    print(val1," ",val2"are coprimes")
else:
    print(val1,val2"are o co primes")
    