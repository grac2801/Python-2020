
#Date: December 10, 2020
#ogracias
#Current Module: homework.iteration
#AP Computer Science Principles

#imports, variables, CONSTANTS




#functions



if __name__ == "__main__":
    
    
    #Use of continue
    myList = list(range(10))
    print('Original:', myList)
    for i in range(len(myList)):
        if i == 5:
            continue
        else:
            print(i, end=" ")
    print('\nEnd of for loop using continue!')
    print('\n')
    
    
           
    #Use of break
    myList = list(range(10))
    print('Original:', myList)
    for i in range(len(myList)):
        if i == 5:
            break
        else:
            print(i, end=" ")
    print('\nEnd of for loop using break!')
    
    
    print()
    print('\n\n----- Parallel processing lists using indices -----')
    metals = ['Li', 'Na', 'K']
    weights = [6.9, 22.98, 39.1]
    for i in range(len(metals)):
        print('Element:', metals[i], ' = ', 'Mass:', weights[i])
    
    
    
    
    
    numberList = list(range(1, 15))  
    print('\n\n--- Practical use of break and continue ---')
    #I want to skip all numbers divisible by 2 or 3
    for i in numberList:
        if i % 2 == 0 or i % 3 == 0:
            continue
        print('Number selected:', i)
    print('final list: ' , numberList, '\n\n')
    
    
    
    #Make new list with selected items
    NotDivBy2Or3 = list()
    print('NotDivBy2Or3 = ', NotDivBy2Or3)
    print('numberList = ' , numberList)
    for i in range(len(numberList)):
        if numberList[i] % 2 == 0 or numberList[i] % 3 == 0:
            continue
        NotDivBy2Or3.append(numberList[i])
    print('final numberList = ', numberList)
    print('NotDivBy2Or3 = ', NotDivBy2Or3)
    print()
    
    
    
    print('----- Student activity -----')
    #Remove all numbers that are even. Print the new list
    numbers = [3, 6, 1, 2, 89, 76, 34, 52, 99, 12, 78]
    allOdds = list()
    for i in range(len(numbers)):
        if numbers[i] % 2 == 1:
            allOdds.append(numbers[i])
    print(allOdds)