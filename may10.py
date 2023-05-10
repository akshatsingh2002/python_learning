# class student:
#     def __init__(self):
#         print("vaue")
#     def __init__(self):
#         print("value")
# # consturctor are the functions which are going to be exectuted when you call the class
# obj = student()
 
 
# class student:
#     def __init__(self,val,name):
#         self.val= val
#         self.name = name
#         print(self.val,self.name)
#     def info(self):
#         print(self.val,self.name)
        
# obj = student(19,"akshat")
# obj2  = student(10,"aman")
# obj.info()
# obj2.info()
        
        
class hobbies:
    def __init__(self,sname,email,hobby):
        self.hobby = []
        self.sname = sname
        self.email = email
        (self.hobby).append(hobby)

    def info(self):
        print(self.sname,self.email,self.hobby)
        
        
    def more(self,val):
        (self.hobby).append(val)
        
        
s1 = hobbies("akshat","akshat@gmail.com","swimming")
s1.more("circket")
s1.more("volleyball")

s1.info()        
