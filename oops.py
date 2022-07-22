class webserires:
    # show_name="chernobyl"
    # show_length="6"
    def __init__(self,show_name,show_length):
        self.show_name=show_name
        self.show_length = show_length
        
    def episode_(self):
     return f'{self.show_name},{self.show_length}'
    
    
obj = webserires("chernoby",1)
obj2=obj.episode_()
print(obj2)