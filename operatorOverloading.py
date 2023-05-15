class parent:
    def __init__(self,x):
        self.x = x
        
    def __lt__(self,other):
        if self.x < other.x:
            return False
        else:
            return True
        
obj1 = parent(10)
obj2 = parent(20)
print(obj1<obj2)
        