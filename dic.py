lst_ = {
    'str': [],
    'int': [],
}
con=int(0)
n = int(input('enter the number of inputs: '))
for i in range(n):
    dtype = input('enter datatype: ')
    if(dtype=='str'):
        data = input('enter the string: ')
        lst_['str'].append(data)
    elif dtype=='int':
        data = input("enter the int value: ")
        lst_['int'].append(data)
    else:
        
         if con==0:
              lst_.update({'other':[]})
              con=con+1
              
         data = input("enter the vlaue: ")
         lst_['other'].append(data)
        
print(lst_)
