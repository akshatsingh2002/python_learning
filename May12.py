# class student:
#     __x= 10
    
# class childeren(student):
#     y = 10
# print(dir(student))
# print(childeren._student__x)


# class Addnumber:
#     def __init__(self,x,y):
#         self.x =x 
#         self.y=y
        
        
#     def __str__(self):
#         return f"this repr is working ,self.x,self.y)"
   
        
#     def __add__(self,obj):
#         self.x = self.x + obj.x
#         self.y = self.y + obj.y
#         # return self.x,self.y
#         return Addnumber(self.x , self.y)
        
  

# a1 = Addnumber(10,20)
# a2 = Addnumber(10,20)
# # print(a1+a2)
# a1+a2
# print(a1)


# from abc import ABC,abstractmethod
# class dog:
#     @abstractmethod
#     def info(self):
#         pass
        
        
# class fish(ABC):
    
#     def info(self):
#         print("i have zero leg")    
    
#     def info2(self):
#         print("i am a fish")
        
        
# obj = fish()
# obj.info()
# obj.info2()

