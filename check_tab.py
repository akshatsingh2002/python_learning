from turtle import Turtle


def chk(s):
    file=open('tab.txt','r')
    var = file.readlines()
    for i in range(1,len(var)):
        if(int(var[i])-int(var[i-1])==2):
            con =1 
        else:
            con = 0
            break
    
    if con == 1:
        return True
    else:
        return False
    
    
two = chk(2)
print(two)
    