class driver:
    def __init__(self,name,number):
        self.name = name 
        self.number = number
        
    def info(self):
        print(self.name,self.number)
        

class customer(driver):
    def __init__(self, name, number,email):
        super().__init__(name, number)
        self.email = email
    def info(self):
        super().info() 
        print(self.email)
    
    
c1 = customer("akshat",123,"akshat@gmail.com")
c1.info()
print(c1.name)