# for i in range(0,5):
#     for k in range(0,5-i-1):
#         print(" ",end='')
#     for j in range(0,i+1):
#         print("*",end='')
        
#     print()
    
    

    
    
# for i in range(0,5):
#     for k in range(0,5-i-1):
#         print(" ",end='')
#     for j in range(0,i*2-1):
#         if(j%2==0):
#             print("*",end='')
#         else:
#             print(" ",end='')
        
#     print()


    
for i in range(0,5):
    for k in range(0,i):
        print(" ",end='')
    for j in range(i*2,4*2-1):
        if(j%2==0):
            print("*",end='')
        else:
            print(" ",end='')
        
    print()