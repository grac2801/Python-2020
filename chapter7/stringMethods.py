
#Date: Nov 30, 2020
#ogracias
#Current Module: chapter7.stringMethods
#AP Computer Science Principles

#imports, variables, CONSTANTS




#functions



if __name__ == "__main__":
    #ALL STRINGS ARE 'IMMUTABLE' [can not be changed]
    myStr = 'good morning'
    
    print('1. capitalize()')
    print('Original string: {}'.format(myStr))
    myStr1 = myStr.capitalize()
    print('modified string: {}'.format(myStr1))
    print('Original string: {}'.format(myStr))
    print(f'Original string using internal f: {myStr}')
    
    
    print('\n\n2. count()')
    myStr = 'I like fruits, cakes, and everything that is sweet'
    print(len(myStr))
    print('How many i letters? ', myStr.count('i'))
    print('How many i letters starting at index 7? ', myStr.count('i', 7))
    print('How many i letters from index 0 thru 10? ', myStr.count('i', 0, 11))
    
    
    print('\n\n3. endswith()')
    print('Does my string end with \'ing\'?')
#     myStr = input('Enter a string: ')
#     print(myStr.endswith('ing'))
    
    
    print('\n\n4. find(s)')
    myStr = 'stupendous'
    print('Does string contain letter 0? ', myStr.find('o'))
    answer = myStr.find('o')
    if answer == -1:
        print('Character not found')
    else:
        print('Character found at index:', myStr.find('o'))
    
    
    print('\n\n5. find(s, beg)')
    myStr = 'stupendous'
    print('Does string contain letter o starting at index 8? ', myStr.find('o', 8))
    
    
    print('\n\n6. find(s, beg, end)')
    myStr = 'stupendous'
    print('Does string contain letter o between indices 4 and 8? ', myStr.find('o', 4, 7))
    
    
    name = 'Lizbeth'
    lastName = 'ComputerScience'
    print('My name is {1}, and my last name is: {0}'.format(name, lastName))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    