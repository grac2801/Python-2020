'''
ogracias
Current Module: chapter3.ProgramFlow
Date: Nov 9, 2020
AP Computer Science Principles
Periods 1, 3
'''
# imports
import math as xmas


# Function
def force(m, a): # parameters
    '''
    (float, float) --> float
    Returns the total force value after multiplying mass x acceleration
    (m = 5.46, a = 17 --> Force = 92.82)
    '''
    forceTotal = m * a
    return forceTotal


def function2(a, b):
    '''
    (float, float) --> float
    It takes the 1st parameter and add the square of the 2nd parameter
    (2.0, 5.0) --> 27.0
    '''
    return a + xmas.pow(b, 2)


def functionPI(c):
    '''
    (float) --> float
    Takes input c and multiplies it by PI
    (27.0) --> 84.82
    '''
    return c * xmas.pi






# More on notes

def print_twice(aaron):
    print(aaron)
    print(aaron)
    
def cat_twice(part1, part2, number):
    cat = part1 + "-" + part2
    print_twice(cat)
    print('They are both', number, 'years old.')
    

#Client code
if __name__ == '__main__':
#     print('----- Use of Force function -----')
#     mass = float(input('Enter mass: '))
#     accel = float(input('Enter acceleration: '))
#     forceAnswer = force(mass, accel)
#     print('The total force is', forceAnswer, 'N')
#     print('----- Use of function2 as parameter for functionPI -----')
#     first = float(input('Enter first number: '))
#     second = float(input('Enter second number: '))
#     print(functionPI(function2(first, second)))
#     answer = functionPI(function2(first, second))
#     print('Rounded to 2 decimal numbers: ${:,.2f}'.format(answer))
    
    print('----- Call a function from within another function -----')
    part1 = input('Enter first name: ')
    part2 = input('Enter second name: ')
    age = int(input('Enter age'))
    cat_twice(part1, part2, age)
    
 
    
    
    
    
    
    
    
    
    
    
    