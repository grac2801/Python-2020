import chapter6.F2temperatureLibrary as temp

#Date: Nov 22, 2020
#ogracias
#Current Module: chapter6.baking
#AP Computer Science Principles

#imports




#functions
def getPreheatingInstructions(fahrenheit):
    celsius = temp.convertToCelsius(fahrenheit)
    celsius = round(celsius, 3)
    fahrenheit = round(fahrenheit, 3)
    fahr_String = myString(fahrenheit)
    return 'Summary: ' + fahr_String + '\u2103 are equal to:'+ myString(celsius) + '\u2103'

if __name__ == "__main__":
    fahrenheit = float(input('Enter the degrees F: '))
    print(getPreheatingInstructions(fahrenheit))