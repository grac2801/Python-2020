'''
Created on Oct 27, 2020

@author: ogracias
'''
#Addition of integers
sumTotal = 3 + 4
print("total: ", sumTotal)

#Addition of doubles
doubleNumbers = 5.0 + 8.87
print("doubleNumbers: ", doubleNumbers)

#Automatically converts int to floats
convertedUp = 5.0 - 3
print("convertedUp", convertedUp)

#Division and integer division
myDivision = 53/24
print('myDivision', myDivision)

#integer division
myDivision1 = 53//24
print('myDivision1', myDivision1)

#modulo
days = 900
numberOfYears = days // 365.25
print('Number of years: ', numberOfYears)

daysLeftOver = days % 365.25
print('Number of daysLeftOver: ', daysLeftOver)

#Binary operators above. Unary operators 
# Negation symbol

negativeNumber = -5
print("negativeNumber: ", negativeNumber)

negativeNumber = --5
print("- negativeNumber: ", negativeNumber)


fractionalValues = (2/3) + (6/3)
print('fractionalValues: ', fractionalValues)

print('fractionalValues rounded: ', round(fractionalValues, 2))


#PEMDAS precedence order
examplePrecedence = 10 + 20 / 3
print(examplePrecedence)


examplePrecedence = (10 + 20) / 3
print(examplePrecedence)

examplePrecedence = 1 + 1.7 + 3.2 * 4.4 - 16 / 3 
print('examplePrecedence', examplePrecedence)

#Variables
# Fahrenheit to Celsius: F - 32 * (5/9)
FahrenheitDegrees = 212 # error, needs parenthesis
celsiusDegrees = (FahrenheitDegrees - 32) * (5/9)
print(celsiusDegrees)

#Warning = is not equality in Python
#Reassigning variables
difference = 20
print("difference : ", difference)
double = difference * 2
print('double:', double)
difference = 5
print("difference : ", difference)
print('double:', double)
print("\n\n")

#Another example
number = 3
print('number:', number)
number = 2 * number
print('number:', number)
number = number * number
print('number:', number)
number *= number;
print('number:', number)

#More Augmented examples
print()
score = 50
print("score: ", score)
score += 20
print("score: ", score, "\n")

dayz = 2
dayz *= 3 + 4
print('dayz: ', dayz)


degrees_Celsius = 26
print(id(degrees_Celsius))
degrees_madeUp = 26
print(id(degrees_madeUp))
degreesKelvin = 260
print(id(degreesKelvin), "\n\n")

print("Hello, this is Mr. Gracias\
How are you??")

