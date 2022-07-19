map_ ={}

i =0
while i<1:
    imp = input()
    lst=imp.split()
    if(lst[0]=="stop"):
        break
    else:
     key = lst[0]
     val=lst[1]
     if key in map_:
        map_[key].add(val)
     else:
         map_.update({key:set()})
         map_[key].add(val)
         


print(map_)