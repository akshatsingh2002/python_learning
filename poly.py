from calendar import c


class a1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return f'{self.a} +{self.b}'




class a2(a1):
    def __init__(self, a, b):
        super().__init__(a, b)
    def add(self):
        return self.a *self.b
    

obj2=a2(4,5)
obj1=obj2.add()
print(obj1)