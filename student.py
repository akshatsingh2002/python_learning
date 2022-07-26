class student:
    def __init__(self,fname,id):
        # print("hello")
        # id_ = 1 
        self.fname = fname
        self.id = id 
    def print_values(self):
        print(self.fname, self.id)
obj1 = student("akshat",1)
# print(obj1.fname,obj1.id)
obj2 = student("arpit",2)
# print(obj2.fname,obj2.id)
# obj2 = student()
# obj2.fname="aman"
# print(obj2.fname)
obj1.print_values()
obj2.print_values()