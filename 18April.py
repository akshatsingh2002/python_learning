# age = 10
# salary = 10
# print(id(age))
# print(id(salary))
# age = 20
# print(id(age))
# print("testing ", age)
# print(f"testing {age}")
# answer = f"this is string formatting{age}"
# print(answer)
# answer = "this is string formatting {}".format("val is here")
# print(answer)

val = .5
s = ("%0.10f"%(val)) #string fromatting . precision
print(type(s))
print(s)
print(s[5:0:-1]) # starting position, ending position and step