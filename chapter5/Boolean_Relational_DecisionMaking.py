'''
Created on Nov 16, 2020

@author: ogracias
'''

#imports




#functions
def is_positive(value):
    '''
    (float) --> boolean
    Returns True if value > 0, and False if value < 0
    is_positive(5.0) --> True
    '''
    return value > 0

def name():
    '''
    () --> print statement
    Asks user for name and gender, and then prints out whether it is a
    male or female
    name() --> Is Jane female? True
    '''
    name =  input('Enter your first name? ')
    gender = input('Enter your gender M/F ')
    is_female = 'F' in gender
    print('Is', name, 'female? ', is_female)


#--------------------------------------------------------------------------

print('--- Boolean values ---')
print(True)
print(False)
print(not True)
print(not False)

print('\n--- and/or ---')
print('True and True: ', True and True)
print('True and False: ', True and False)
print('False and True: ', False and True)
print('False and False: ', False and False)


print('\n--- or gate ---')
print('True or True: ', True or True)
print('True or False: ', True or False)
print('False or True: ', False or True)
print('False or False: ', False or False)


print('\n--- Building expressions ---')
b1 = False
b2 = False
print((b1 and not b2) or (b2 and not b1))


b1 = False
b2 = True
print((b1 and not b2) or (b2 and not b1))


b1 = True
b2 = False
print((b1 and not b2) or (b2 and not b1)) #short circuit


b1 = True
b2 = True
print((b1 and not b2) or (b2 and not b1)) 

print('\n--- Building expressions ---')
cold = True
windy = False
print((not cold) and windy)
print(not(cold and windy))


print('\n--- Relational operators ---')
'''
>    Greater than
<     Less than
>=  Greater than or equal to
<=  Less than or equal to
==  Equal to
!=  Not equal to
'''
print(45 > 34)
print(45 > 79)
print(45 < 79)

print('\n--- Compare floats ---')
print(23.1 > 23)
print(23.1 >= 23.1)

print(67.3 == 87)
print(67 == 67.00001)
print(67 != 67.00001)


print('\n--- Function with returned boolean ---')
#Ask user for a number
#Pass number to a function
#Return True if value > 0, and False is value < 0
# number = float(input('Enter a number: '))
# print(is_positive(number))



print('\n--- Levels of precedence ---')
'''
Highest priority =     *, /, +, -
next highest =        <, >, !=, ==
Lowest priority =    and, or, not
'''
x = 2
y = 5
z = 7
answer = (x < y) and (y < z)
print('answer: ', answer)
answer = x < y and y < z
print('answer: ', answer)


print('\n--- Combine comparisons ---')
x = 5
print('Is value between 1 and 5? ')
OneAndFive = (1 < x ) and (x <= 5)
print(OneAndFive)

print('\n--- Combination surprises ---')
first =  3 < 5 != True

second =  3 < 5 != False
print('first: ', first, 'second: ', second)

empty = ''#By default, an empty string is false in Python
print('not empty: ', not empty)


print('\n--- Compare strings ---')
print('A < a: ', 'A' < 'a')
print('abc < abcd', 'abc' < 'abcd')
print('jan' in 'The baby was born in Jan 2020')

#student program
#Ask user to input a name and a gender within the function
#Return a print statement saying whether the user is male or female
#Is Jane female? True

name()





