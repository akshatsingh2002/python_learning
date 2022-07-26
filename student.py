# class student:
#     def __init__(self,fname,id):
#         # print("hello")
#         # id_ = 1 
#         self.fname = fname
#         self.id = id 
#     def print_values(self):
#         print(self.fname, self.id)
# obj1 = student("akshat",1)
# # print(obj1.fname,obj1.id)
# obj2 = student("arpit",2)
# # print(obj2.fname,obj2.id)
# # obj2 = student()
# # obj2.fname="aman"
# # print(obj2.fname)
# obj1.print_values()
# obj2.print_values()
from email.message import EmailMessage


class driver:
    def __init__(self,id,name,email):
        self.name=name
        self.id=id
        self.email=email
    
    def print_info(self):
        print(self.id,self.name,self.email)
        
class customer(driver):
    def __init__(self, id, name, email,wallet):
        super().__init__(id, name, email)
        self.wallet = wallet
    def print_info(self):
        return super().print_info()
    
    
    
obj1 = customer(1,"akshat","google.com","2 rs")
obj2 = driver(22,"arpit","bnaiya")
obj2.print_info()
obj1.print_info()
