a = input()
lst1 = a.split()
r = int(lst1[0])
c = int(lst1[1])
str1 = ""
str2 = ""
str3 = ""
for i in range(1,c):
    str1 =str1 + "."
    str2 =str2 + "."
    str3 =str3 + "#"

str1 = str1+"#"
str2 ="#" + str2
str3 = str3 + "#"
# print(str1,str2)
for j in range(0,r):
    
    if j==0 or j%2==0:
        print(str3)
        
    elif j%3==0:
        print(str2)
        
    else:
        print(str1)