#Date: Dec 7, 2020
#ogracias
#Current Module: chapter9.forLoops
#AP Computer Science Principles

#imports, variables, CONSTANTS




#functions



if __name__ == "__main__":
    print()
    print('----- Simple loop -----')
    myFriends = ['Juan', 'John', 'Joan']
    for i in myFriends:
        print(i)
    
    print()
    print('----- Conversion -----')
    
    velocities = [0.0, 9.81, 19.62, 29.43]
    for velocity in velocities:
        print('English:', velocity, 'inches. Metric:', velocity * 2.54, 'cm.')


    print()
    print('----- Traversing a string -----')
    country = 'United States of America'
    for ch in country:
        if ch.isupper():
            print(ch, end='')
            
            
    print()
    print('----- built-in range function -----')
    range(10) #number not included. It is exclusive
    for i in range(10):
        print(i, end=', ')
    
    print()
    print('----- Using a list -----')
    #making a list out of all numbers within the range
    print(list(range(10)))
    
    #Adding a step and a specific slice [Use a comma)
    print(list(range(1, 11)))
    
    #Number of possible years from the year 2000 to today 2020
    print(list(range(2000, 2021, 4)))
    
    #You can always go backwards
    #Example: Years from 2050 - 2020 inclusive
    print(list(range(2050, 1998, -4)))
    
    print()
    print('----- Add all numbers from 1 to 100 -----')
    total = 0
    for i in range(1, 101):
        total += i
        print('iteration #', i, '= ', total)
    print(total)
    
    #Less control but same result
    a = list(range(1, 101))
    print(sum(a))
    
    
    print('\n\n')
    total = 0
    for i in range(1, 101):
        total += i
        if i == 50:
            print('iteration #', i, 'ANSWER:', total)
            continue
        print('iteration #', i, '= ', total)
    print("total sum: ", total)
    
    
    print()
    print('----- Processing lists using indices -----')
    #This does not change the value of the items in a list
    values = [4, 10, 3, 8, -6]
    print('before:', values)
    for num in values:
        num = num * 2
    print('after:', values)
    
    
    #See their actual values using the range built-in function
    for i in range(len(values)):
        print('i:', i, 'value:', values[i])
    
    
    #Use the indices of the items in the list to change their values
    values = [4, 10, 3, 8, -6]
    print('\n\nbefore:', values)
    for num in range(len(values)):
        values[num] = values[num] * 2
    print('after:', values)
   
    print()
    print('\n\n----- Parallel processing lists using indices -----')
    metals = ['Li', 'Na', 'K']
    weights = [6.9, 22.98, 39.1]
    for i in range(len(metals)):
        print('Element:', metals[i], chr(8669), 'Mass:', weights[i])
    
    
    
    print()
    print('----- Student activity -----')
    #Remove all numbers that are even. Print the new list
    numbers = [3, 6, 1, 2, 89, 76, 34, 52, 99, 12, 78]
    allOdds = list()
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            allOdds.append(numbers[i])
    print(allOdds)
    
    
    print()
    print('----- Nested loops -----')
    outer = ['Li', 'Na', 'K']
    inner = ['F', 'Cl', 'Br']
    for metal in outer:
        for halogen in inner:
            print(metal + halogen)
            
    
    print()
    print('----- multiplication table -----')
    
