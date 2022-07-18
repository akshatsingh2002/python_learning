name = input("enter the password ")
l = len(name)
for i in range(l):
    if ord(name[i])>=65 and ord(name[i])<=122:
        print('yes')
        break