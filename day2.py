# print ( ord('a') ) #returns the ascii value of the string 
# print ( chr (66) ) #returns the string of the ascii  value
# s = 'Arpit '
# b = ' Baniya '
# print ( s + b + 'op')
# full_name = '{first_name} {last_name}'.format(first_name = ' Akshat '  ,last_name = ' Singh ')


# print ( full_name )
# name = input ( "enter your name: ")
# sem = input ("enter your semister: ")
# college = input ("enter your college name: ")
# sentence = '{} is in {} of {} college'.format(name,sem ,college)
from unittest.mock import sentinel


# sentence = "how are you"
# print(sentence.count('o'))
# print(sentence.strip('how'))
# print(sentence.find('are'))
# print(sentence)
first_name = 'Akshat'
last_name = 'Singh'
sentence = f'{first_name} {last_name}'
print(sentence)

#capatalized function to make the first character of the string capital