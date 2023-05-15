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




# class dollar:
#     def __init__(self,amount):
#         self.amount = amount
    
#     def __repr__(self):
#         return f"this the the wrapper working ${self.amount}"
#     @classmethod
#     def amount1(cls,num1,num2):
#         return cls(num1+num2)
        
        
# # obj = dollar(10)
# # print(obj.amount1(10,20))
# # print(obj)


# class euro(dollar):
#     def __init__(self,amount):
#         super().__init__(amount)
#         self.symbol = "x"
#     def __repr__(self):
#         return f" the amount is Yen {self.amount}  { self.symbol}"
    


# a1 = euro(99)
# a1.amount1(99,100)
# print(a1)

# lst = []
# print(dir(lst))


s = "akshat"
obj =iter(s)
print(next(obj))
# def hello(num):
#     print("hello")
#     yield num
#     print("hi")
#     yield 2
#     yield 3


# x = hello(1)
# for i in x:
#     print(i)
# print(x)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())



