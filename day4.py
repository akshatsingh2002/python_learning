# tup = (1,2,3,4,'hello world')
# print(tup)
# # tupples are immutable 
# lst = [1,2,3,4]
# tup2 = tuple(lst)
# print(tup2)
# fname = 'akshat'
# print(list(fname))

# in sets we dont see elements repeated
lst = {1,22,3,3,4,4}
print(lst)
lst.add(5)
print(lst)
lst2 = {9,10,11}
print(lst.union(lst2))
# we cant access elements of list by indexing
print(len(lst))
lst2.add(3)
lst.difference_update(lst2)
print(lst)
lst.discard(4)
print (lst)

