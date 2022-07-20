# def hello():
#     print("greet")
#     return 
# hello()
# var = hello()
# print(var)

def fact(n):
 f=1
 for i in range(1,n+1):
     f=f*i
 return f

var = fact(6)
print(var)