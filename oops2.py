from io import BufferedRandom


class vehicle:
    def __init__(self , brand):
        self.brand = brand
        
        
    def get_brand(self):
        return f'thi is the branch {self.brand}'
class car(vehicle):
     def __init__(self, brand, type_ , engine):
         super().__init__(brand )
         self.type_ = type_
         self.engine = engine
        
     def get_type_color(self):
        return f' {self.brand} {self.type_} {self.engine}'
             
    
    
    
    
    
obj1=car("Lexus","sports","V10")
obj2=obj1.get_type_color()
print(obj2)