# class student:
#     @staticmethod
#     def info(x,y):
#         print(x,y)
        
# student.info(10,20)



# class student:
#     @classmethod
#     def info(cls):
#         print(cls.__name__)
        
# student.info()




class dollar:
    def __init__(self,amount):
        self.amount = amount
    
    def __repr__(self):
        return f"this the the wrapper working ${self.amount}"

    def amount1(self,num1,num2):
        return dollar(num1+num2)
        
        
obj = dollar(10)
print(obj.amount1(10,20))
print(obj)