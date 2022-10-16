# for i in range(0,5):
#     for j in range(0,i):
#         print("*",end='')
#     print("\n")
from re import S

from numpy import empty

# every memory leocation is isolated from each other in case of objects
class employee:
    def __init__(self,e_id,e_name,email,e_salary): #all these vairabls are called instance variable 
        self.e_id = e_id
        self.e_name = e_name
        self.email = email
        self.e_salary = e_salary
        
    def getvalues(self):
        print(self.e_name,self.email,self.e_salary)
        
        
class employee2(employee):
    def __init__(self, e_id, e_name, email, e_salary,status):
        super().__init__(e_id, e_name, email, e_salary)
        self.status =status 
    def getvalues(self):
        return print(self.e_name,self.email,self.e_salary,self.status)

obj1 = employee2(1,"akshat","aksahat@gmail.com",100000,"running")
obj2 = employee2(2,"aman","amain@gmal.com",10,"running")
obj1.getvalues()
obj2.getvalues()

#import os , pyautogui , selenium , matplotlib , seborn, datascience , numy , pandas ,  scikitlearn , tenserfow , scipy
# generators are important 