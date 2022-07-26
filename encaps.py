class vehicle:
    _year = 1000 #notation for protected modifier   
    __price = 100000 # this is the pricate variable

class tata(vehicle):
    car_name="harrier"
    
obj1=tata()
obj2 = vehicle()
print(dir(obj2))
print(obj2._vehicle__price)
print(obj1._year,obj1.__price)
