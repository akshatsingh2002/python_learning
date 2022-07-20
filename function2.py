# from function import fact
# def return_list():
#     lst_=[1,2,3]
#     return lst_


# var = return_list()
# print(var)
# var2 = fact(6)

# def caps(s):
#  sum_ = int(0)
#  for i in s:
#      sum_ = sum_ + ord(i)
#  return sum_
   
   
# var = caps("akshat")
# print(var)
# def passgen(username,password):
#     return username[:4:]+password[-4::]
    
# var = passgen('akshat','heassswwsllo')
# print(var)
# def big(s):
#     count_ = 0 
#     l = len(s)
#     for i in range(1,l):
#         if(ord(s[i])==ord(s[i-1])+1):
#             count_+=1
            
    
#     return count_

# var = big("aabbadc")
# print(var)
        
def even(lst):
    for i in range(len(lst)):
        if(lst[i]%2==0):
            print(lst[i])
            
            
even([1,2,3,4,5,6,7])
    
