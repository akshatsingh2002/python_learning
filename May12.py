# class student:
#     __x= 10
    
# class childeren(student):
#     y = 10
# print(dir(student))
# print(childeren._student__x)


class Addnumber:
    def __init__(self,x,y):
        self.x =x 
        self.y=y
        
        
    def __repr__(self):
        print("this repr is working",self.x,self.y)
   
        
    def __add__(self,obj):
        self.x = self.x + obj.x
        self.y = self.y + obj.y
        # return self.x,self.y
        return Addnumber(self.x , self.y)
        
  

a1 = Addnumber(10,20)
a2 = Addnumber(10,20)
# print(a1+a2)
a1+a2
