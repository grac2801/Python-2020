
#Date: Dec 2, 2020
#ogracias
#Current Module: chapter8.lists
#AP Computer Science Principles

#imports, variables, CONSTANTS




#functions



if __name__ == "__main__":
    print()
    print('----- Syntax for a list -----')
    daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
    print(daysOfTheWeek)
    numberList = [1, 5, 6, 2, 9, 12]
    print(numberList)
    mixedList = ['Roberto', 2.5, 9, 3.4]
    print(mixedList)
    combinedList = [numberList, mixedList]
    print('Combined list:', combinedList)
    #Isolate just one item via its index syntax
    print(mixedList[0])
    print(combinedList[1][0])
    
    print()
    print('----- offset -----')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes[4], '=', marxes[-1])
    # list[beg : end(exclusive)
    print(marxes[0:4])
    print(marxes[0:5])
    print(marxes[0:3])
    print(marxes[:])
    
    print()
    print('----- change items in a list -----')
    marxes[2] = 'Anahi'
    print(marxes)
    # list[beg : end : step)
    print(marxes[::2])
    
    
    print()
    print('----- append() -----')
    marxes.append('Raphael') # adds item to the end of the list
    print(marxes)
#     print(marxes.append('anotherName'))
    
    
    print()
    print('----- extend() -----')
    print(marxes)
    extendedList = ['extended1', 'extended2']
    marxes.extend(extendedList)
    print(marxes)
    
    
    print()
    print('----- Concatenation (+=) -----')
    others = ['Gummo', 'Karl']
    print(marxes)
    #Let's concatenate
    marxes += others
    print(marxes)
    
    
    print()
    print('----- pop() -----')
    #By default pop() removes last item in list
    marxes.pop()
    print(marxes)
    
    #You can also remove any other item by index value
    marxes.pop(0)
    print(marxes)
    
    
    print()
    print('----- find the index -----')
    print(marxes.index('Raphael'))
    is_here = 'Raphael' in marxes
    print('is Raphael found in the list? ', is_here)
    
    