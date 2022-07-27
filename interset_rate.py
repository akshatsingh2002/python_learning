import email


class employee_detail:
    def __init__(self,id,emailid,salary,year):
        self.id = id
        self.emailid = emailid
        self.salary = salary
        self.year = year 
    
    def print_info(self):
        print(self.id,self.emailid,self.salary,self.year)

class employee(employee_detail):
    def __init__(self, id, emailid, salary, year,time,rate):
        self.time=float(time)
        self.rate=rate
        super().__init__(id, emailid, salary, year)
    def print_info(self):
        print(self.id,self.emailid,self.salary,self.year)
        print("salary per month: ",(self.salary)/12)
        print(self.salary*((1+self.rate)**self.time)-self.salary)
        
obj1=employee(1,'something@gmial.com',200000,2002,2,0.2)
obj1.print_info()