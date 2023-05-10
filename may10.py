# class student:
#     def __init__(self):
#         print("vaue")
#     def __init__(self):
#         print("value")
# # consturctor are the functions which are going to be exectuted when you call the class
# obj = student()
 
 
class student:
    def __init__(self,val,name):
        self.val= val
        self.name = name
        print(self.val,self.name)
    def info(self):
        print(self.val,self.name)
        
obj = student(19,"akshat")
obj2  = student(10,"aman")
obj.info()
obj2.info()
        