class driver:
    def __init__(self,name,number):
        self.fname = name 
        self.number = number
        
    def info(self):
        print(self.fname,self.number)
        

class customer(driver):
    def __init__(self, name, number,email):
        super().__init__(name, number)
        self.email = email
    def info(self):
        super().info() 
        print(self.email)
    
    
c1 = customer("akshat",123,"akshat@gmail.com")
c1.info()
print(c1.fname)