class user:
    def __init__(self , name , contact ):
        self.name = name
        self.contact = contact
    def get_user_data(self):
        return f'The name of the person is {self.name} {self.contact}'
    
class baniya_sector(user):
    def __init__(self, name, contact, money, bank):
        super().__init__(name, contact)
        self.money= money
        self.bank = bank
    def get_money(self):
      return f' rokda = {self.money}'

class all_data(baniya_sector):
    def __init__(self, name, contact, money, bank):
        super().__init__(name, contact, money, bank)
    def get_all_data(self):
        return f' {self.name} {self.contact} {self.money} {self.bank}'
    
    
    
obj1=all_data("arpit_agarwal","1001001001","1cr","jain secure bank")
obj2=obj1.get_all_data()
print(obj2)