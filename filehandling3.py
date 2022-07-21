from dataclasses import field


def frequency(s):
    
    map_={}
    file = open(s,'r')
    data_ = file.read()
    lst_ = data_.split()
    file.close()
    file = open('newfile.txt','w')
    for i in lst_:
        if i in map_:
            map_[i] += 1

        else:
            map_[i] = 1
            
        
        file.write(i)
        file.write(" ")
        
        file.write(str(map_.get(i)))
        
        file.write("\n")
    return map_
    file.close()
    
        
var = frequency('wiki.txt')