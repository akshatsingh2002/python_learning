# n = int(input("Enter to check whether the number is enevn or not"))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# a = float(input("A"))
# b = float(input("B"))
# c = a / b
# print(c10)


# a = 1
# b = 2
# n = int(input("Enter the finbonacci range"))
# if n == 1:
#     print(a)
# elif n == 2:
#     print(b)
# else:
#     for i in range(1,n+1):
#         if i == 1:
#             print(a)
#         elif i == 2:
#             print(b)
#         else:
#             c = a+b
#             print(c)
#             a = b
#             b = c



# mystr = input("enter the string")
# mydict = {}
# for i in mystr:
#     if i in mydict:
#         mydict[i]+=1
#     else:
#         mydict[i]=1
#
# print(mydict)

# mylist = ['1','hello','world','?']
# mydict = {}
# for i in range(0,len(mylist)):
#     mydict[i]=mylist[i]
# print(mydict)


# file = open('smaple.txt','r')
# file = file.readline()
# mydict ={
# }
# for i in file:
#     if i in mydict:
#         mydict[i]+=1
#     else:
#         mydict[i]=1
# print(mydict)

# file = open("smaple.txt","r")
# s = file.readline()
# l = len(s)
# for i in range(l-1,-1,-1):
#     print(s[i])
# extension = ("sample.txt").split(".")
# for i in extension:
#     if i == "txt":
#         print("textfile")
#     elif i == "py":
#         print("pythonfile")


# from difflib import SequenceMatcher
# a = input("Enter string a")
# b = input("Enter string b")
# c = SequenceMatcher(None,a,b).ratio()
# if(c*100>80):
#     print("The string are nearly equal")
# else:
#     print("the strings are not nearly equal")
# import fractions
# a = int(input("Enter the first number"))
# b = int(input("Enter the second number"))
# gcd1 = fractions.gcd(a,b)
# print(gcd1)
# print((a*b)/gcd1)

r1 = int(input("Enter r1"))
c1 = int(input("Enter c1"))
r2 = int(input("Enter r2"))
c2 = int(input("Enter c2"))
if(c1!=r2):
    print("cannot mulitply matrix")
else:
    print("Enter the data in first matrix")
    mat1=[]
    for i in range(0,r1):
        temp = []
        for j in range(0,c1):
            val = int(input ())
            temp.append(val)
        mat1.append(temp)
    print("Enter the data in the second matrix")
    mat2=[]
    for i in range(0,r2):
        temp = []
        for j in range(0,c2):
            val = int(input ())
            temp.append(val)
        mat2.append(temp)

    mat3=[]
    for i in range(0,r1):
        temp=[]
        for i in range(0,c2):
            temp.append(0)
        mat3.append(temp)

    for i in range(0,r1):
        for j in range(0,c2):
            for k in range(0,c1):
                mat3[i][j]+=mat1[i][k]*mat2[k][j]

    print(mat3)

