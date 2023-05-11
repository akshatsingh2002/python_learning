# class driver:
#     def __init__(self,name,number):
#         self.fname = name 
#         self.number = number
        
#     def info(self):
#         print(self.fname,self.number)
        

# class customer(driver):
#     def __init__(self, name, number,email):
#         super().__init__(name, number)
#         self.email = email
#     def info(self):
#         super().info() 
#         print(self.email)
    
    
# c1 = customer("akshat",123,"akshat@gmail.com")
# c1.info()
# print(c1.fname)

##class variables

# class CounterValue:
#     count = 0
#     def __init__(self):
#        CounterValue.count += 1
       
       
# c1 = CounterValue()
# c2 = CounterValue()
# print(CounterValue.count)


# class DataScience:
#     def info(self):
#         print("this is the datascience class")
        
# class child(DataScience):
#     def info1(self):
#         super.info()
        
        

# class child2(child):
#     def info2(self):
#          super.info1()
        
        
# obj = child2()
# obj.info2()


class first:
    def info(self):
        print("this is the first class")
        
class second:
    def info2(self
              ):
        print("this is the second class")
        
class third(first,second):
    def final(self):
        super().info()
        super().info2()
        
        
obj = third()
obj.final()