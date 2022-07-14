# a = 5
# b = 6 
# print ( "The addition is " )
# print ( a + b)
# print ( "The subtraction is " )
# print ( a - b)
# print ( "The multiplication is " )
# print ( a * b)
# print ( "The division is " )
# print ( a / b)
# print( type (a) )
# comp = 5 + 9j
# print( type (comp) ) 
# sentence = input("enter stirng")
# str2=sentence[::-1]
# if sentence==str2 :
#     print ( "yes this is an palindrome ")
# else :
#     print ( " this is not palindrome ")
option = input( "select 1 for squar , 2 for circle and 3 for rectangel  , 4 for  right angle triangle" )
if int(option)==1:
    side = input ("Enter the length of the square ")
    print ( int(side)*int(side))
elif int(option)==2:
    radius = input ("enter the radius of the circle")
    print ( 2*3.14* int(radius))
elif int(option)==3:
    l = input ("enter the length of the rectangel")
    b = input ("enter the breadth of the rectangel")
    print ( int (l) * int (b) )
elif int(option)==4:
    l = input ("enter the height of the triangle")
    b = input ("enter the base of the triangle")
    print ( 0.5 * int (l) * int (b) )
else :
    quit()