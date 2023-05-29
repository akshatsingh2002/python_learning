import numpy 

arr = numpy.array([[1,2,3],[4,5,6]])
arr = arr + 3
print(arr)
print(arr.shape)
print(arr.ndim)
arr = arr  - 3 
print(arr)
print(arr.shape)
print(arr.ndim)
arr = arr * 3
print(arr)
print(arr.shape)
print(arr.ndim)
arr = arr / 3
print(arr)
print(arr.shape)
print(arr.ndim)

arr = arr +[1,2,3]
print(arr)
print(arr.shape)
print(arr.ndim)

# arr = arr +[1,2,3,4] blog here 
# print(arr)
# print(arr.shape)
# print(arr.ndim)


# arr2 = numpy.array([1,2,3,4]) #first rank array
# print(arr2.ndim) here
# print(arr2.shape)

# print(type(arr))