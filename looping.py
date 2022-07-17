# lst = [1,2,3,4,5,6,7,8,9]
# for i in range(0,len(lst),2):
#     print (lst[i])
    
    
# str = 'akshat'
# for i in str:
#     print(i)
# for i in range(1,6):
#     for j in range(i):
#         print('*',end="")
#     print('\n')
user = int(input("enter the number to check is it prime or not "))
print ( user)
l = int(user/2)
print(l)
con = int(1)
for i in range(2,l):
    # print(i)
    if(user%i==0):
        con=0
        break
    # else:
    #     con = 1
if(con==0):
    print("the number is not prime")
else:
    print("the number is prime")
    