fact = int(input("enter the number to find its factorial"))
fact=fact+1

ans = int (1)
if fact== int(0):
 ans=1
elif fact == 1 :
 ans=1
else:
    for i in range(1,fact):
        ans=ans*i
        
print(ans)