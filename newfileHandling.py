# f = open('testfile.txt','r')
# # print(f.tell())
# print(f.seek(3))
# text = f.read()
# print(f.tell())
# print(text)
# f.close()

with open('testfile.txt','r') as f:
    text = f.readlines()
    print(text)
# text = f.readline()
# print(text)