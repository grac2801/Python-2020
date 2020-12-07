'''
ogracias
Current Module: chapter4.workingWithText
Date: Nov 12, 2020
AP Computer Science Principles
Periods 1, 3
'''

# functions
def convertToCelsius(f):
    celsius = (f - 32) * (5 /9)
    celsiusRounded = round(celsius, 2)
    return celsiusRounded

def printAgain(str1):
    return str1 * 3








# -----------------------------------------------

# Single quotes strings
philosopher = 'Aristotle'
print(philosopher)

mathematician = "Isaac Newton"
print(mathematician)

# wrongName = 'Joseph"
print(len('Albert Einstein'))
print(len(mathematician))
print(len(' '))
print(len(''))

#concatenation
print('Albert' + 'Einstein')
print('Albert' + ' ' + 'Einstein')
print('Albert ' + 'Einstein')
print('Albert' + ' Einstein')

# You can also add an empty string variable
empty = ' '
name1 = 'Joseph'
name2 = 'Doe'
print(name1 + empty + name2)

cpd = 'NH' + myString(3)
print(cpd)
cpd = 'NH' + '\u2083'
print(cpd)

print('9' + ' planets')

print('Four score and ' + myString(7) + ' years ago')

print(int('7'))
print(float('7'))

print(int('4909'))

# The * operator
DNA = 'ATT'
print(DNA * 10)

# Special characters using the escape key (\)
# \', \", \\, \t, \n, \r
print("That's better")
print('That\'s better')

print('C:\\Users\\ogracias')
print('She said: \"That is better\"')
print(len('\"'))
print(len('\u2083'))
print('TAB1\tTAB2\tTAB3\nTAB4')
print('carriageReturn1\rhello')

# multi-line comment
myComment = '''
My name is Mr. Gracias
    I teach APCS P     2020
        Today is Thursday
'''
print(myComment)

print(1, 'two', "three", 4.0)

# variables can be printed as well in a string 
radius = 5
print('The diameter of the circle is', radius, 'cm.')

# help(print)

print('a', 'b', 'c', sep = ', then ', end = '.')
print('\n\n\n')
print(convertToCelsius(80))
print(convertToCelsius(78.8))
print(convertToCelsius(10.4))

print('\n\n\n')
print('80, 78.8, and 10.4 \u2109 are equal to ', end = '')
print(convertToCelsius(498), end = ', ')
print(convertToCelsius(24.87), end = ', and ')
print(convertToCelsius(212), end = ' \u2103')



print('\n\n')
species = input('What species are you? ')
population = int(input('How many bacteria are there? '))
temp = float(input('What is the temperature outside? '))
print(type(species))
print(type(population))
print(type(temp))
























