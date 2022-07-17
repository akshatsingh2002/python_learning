lst_ = {
    'str': [],
    'int': [],
}
n = int(input('enter the number of inputs'))
for i in range(n):
    dtype = input('enter datatype')
    if(dtype=='str'):
        data = input('enter the string')
        lst_['str'].append(data)
    else:
        data = input("enter the int value")
        lst_['int'].append(data)
        
print(lst_)
    