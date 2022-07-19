name = input ( "enter the string ")
name = name.lower()
map_ ={}
for i in name:
    if i  in  map_:
        map_[i] +=1
    else:
        map_[i]=1
      
print(map_)