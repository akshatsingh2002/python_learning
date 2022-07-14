# print ( ord('a') ) #returns the ascii value of the string 
# print ( chr (66) ) #returns the string of the ascii  value
# s = 'Arpit '
# b = ' Baniya '
# print ( s + b + 'op')
# full_name = '{first_name} {last_name}'.format(first_name = ' Akshat '  ,last_name = ' Singh ')


# print ( full_name )
name = input ( "enter your name: ")
sem = input ("enter your semister: ")
college = input ("enter your college name: ")
sentence = '{} is in {} of {} college'.format(name,sem ,college)
print (sentence)