num = input("ENter the number to check whether it is prime our not ")
num = int(num)
con = 0
for i in range(2,num//2):
    if(num%i==0):
        con = 1
        break
    
    
if(con == 0):
    print(num," is prime")

else:
    print(num," is not prime")
