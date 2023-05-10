# f = open('testfile.txt','r')
# # print(f.tell())
# print(f.seek(3))
# text = f.read()
# print(f.tell())
# print(text)
# f.close()

# with open('testfile.txt','r') as f:
#     text = f.readlines()
#     print(text)
# text = f.readline()
# print(text)

# with open('testfile2.txt','a') as f:
#     print(f.tell())

# with open('testfile2.txt','a') as f:
#     text = f.read()
#     print(text)
    
# with open('testfile2.txt','x') as f:
#     text = f.read()
#     print(text)

age = int(input("Enter the age of the candiate"))
try:
    if age < 18 :
        raise Exception
    else:
        print("valid age")
except Exception as e:
    print(type(e))  