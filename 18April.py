age = 10
salary = 10
print(id(age))
print(id(salary))
age = 20
print(id(age))
print("testing ", age)
print(f"testing {age}")
answer = f"this is string formatting{age}"
print(answer)
answer = "this is string formatting {}".format("val is here")
print(answer
      )