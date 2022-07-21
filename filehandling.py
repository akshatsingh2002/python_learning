# file = open('demo.txt','r')
# data = file.readlines()
# print (data)
# file.close()
# file = open('demo.txt','w')
# file.writelines(["hello my name is akshat" ,"and i am from jecrc college"])
# file.close()

# file = open('demo.txt','a')
# file.write("and this is the appended text")
# file.close()

def ipt(s):
    map_ = {}
    for i in range(len(s)):
     lst_ = s[i].split()
     sub = lst_[0]
     val  = lst_[1]
    
     if sub in map_:
        map_[sub].add(val)
     else:
        map_.update({sub:set()})
        map_[sub].add(val)
        
    return map_
    file.close()
    
file = open('demo.txt','r')


file_data = file.readlines()
# print(file_data)
var = ipt(file_data)
print(var)


# def read_file_and_return_map(file_path):
#     file = open(file_path,'r')
#     data = file.readline()
    
            