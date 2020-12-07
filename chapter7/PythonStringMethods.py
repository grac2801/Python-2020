
#Date: 
#Student name: 
#Assignment = String Methods
#AP Computer Science Principles


#imports, variables, CONSTANTS





#functions



if __name__ == "__main__":
   
    # https://www.tutorialspoint.com/python3/python_strings.htm
    
    
    #===========================================================================
    # I will exemplify first 4 String methods
    #===========================================================================
    print('1. Capitalize():')
    name = 'oscar'
    print('You input: {}'.format(name))
    name = name.capitalize()
    print('Capitalized: ', name, end='\n\n')
    
    
    print('2. Count():')
    myString = 'I like fruits, cakes, and everything that is sweet!'
    print('How many i letters? ', myString.count('i'))
    print('There are', myString.count('i', 0, 20), 'i letters in my string', end='\n\n')
    
    
    print('3. endswith(end)')
    print('Does my string end with \'ing\'')
    myStr = 'running'
    print(myStr.endswith('ing'))
    
    
   
    #===========================================================================
    # Now you complete the rest of them in the assignment
    #===========================================================================
    print('\n4. find(s)')
    print('Find the letter o in my string: ')
    myStr = 'stupendous'
    print("Does string contain letter o? ", myStr.find('o'))
    print("Does string contain letter o? ", myStr.find('o', 1, 8))



    print('\n5. find(s, beg)')
    print('Find the letter o in my string: ')
    myStr = 'stupendous'
    #-1 output means NO answer found
    print("Does string contain letter o starting at index 7? ", myStr.find('o', 8))
    
    #Using this in an if else statement
    print('--alternative--')
    temp = myStr.find('o', 7)
    if(temp == -1):
        print("Value was not found")
    else:
        print('Value found in index: ', temp)




    print('\n6. find(s, beg, end)')
    print('Find the letter o in my string: ')
    myStr = 'stupendous'
    #-1 output means NO answer found
    print("String contain letter o between 4 and 7? ", myStr.find('o', 4, 8))
    
    
    
    
    print('\n7. format())')
    myName = 'Oscar'
    myAge = 49
    print('My name is {0}, and I am {1} years old'.format(myName, myAge))
    print('My name is %s , and I am %d years old' % (myName, myAge))
    print('My name is {1}, and I am {0} years old'.format(myName, myAge))
    print(f'My name is {myName}, and I am {myAge} years old.')
    
    
    
    
    print('\n8. isLower()')
    myStr = 'this are all lowercase letters'
    print('Is myStr lowercase?', myStr.islower())
    
    
    
    print('\n9. isUpper()')
    myStr = 'HELLO'
    print('Is myStr uppercase?', myStr.isupper())
    


    print('\n10.lower()')
    myStr = 'The first letter is uppercase'
    myStr.lower()
#     myStr = myStr.lower()
    print(myStr)

    
    print('\n11.lstrip()')
    statement1 = "   --- Hello ---"
    print(statement1)
    print(statement1.lstrip())
    
    
    
    
    
    #lstrip by character
    print('\n12.lstrip(s)')
    statement1 = "---Hello---"
    print(statement1.lstrip('-'))
    
    
    
    print('\n13.replace(old, new, max(optional)')
    myStr = 'Today is a nice day, it is Monday, and this is great!'
    print(myStr.replace(' is ', 'was', 100))
    
    
    
    print('\n14.rstrip()')
    myStr = '   --Please remove trailing dashes---   '
    print(myStr) #dashes still there
    print(myStr.rstrip())
    
    
    print('\n15.rstrip(s)')
    myStr = '--Please remove trailing dashes---'
    print(myStr) #dashes still there
    print(myStr.rstrip('-'))
    
    
    print('\n16.split()')
    school = 'Bonita Vista High School'
    print(school)
    print(school.split())
    
    
    #continued
    school = 'Bonita Vista High School'
    print(school.split('i', 1))#Only one change
    
    
    print('\n17.startswith(beginning) --> boolean')
    myStr = 'Welcome to APCS Principles'
    print(myStr.startswith('W'))
    print('Does index 8 start with letter t? ')
    print(myStr.startswith('to', 8))
    print('Does the string 5 - 6 start with me?')
    print(myStr.startswith('me', 5, 7))
    
    
    
    print('\n18. strip()')
    myStr = '     Welcome to winter winterland     '
    print('Original string:', myStr)
    print('Modified string:', myStr.strip(' '))
    
    
    print('\n19. strip()')
    myStr = '-----Welcome to winter winterland-----'
    print('Original string:', myStr)
    print('Modified string:', myStr.strip('-'))
    
    
    print('\n20. swapcase()')
    myStr = 'Hello Everyone How Are You?'
    modified = myStr.swapcase()
    print(modified)
    
    
    print('\n21. upper()')
    myStr = 'Hello Everyone How Are You?'
    modified = myStr.upper()
    print(modified)
    
    
    print('\n22. title()')
    myStr = 'HELLO everyone HOW are YOU?'
    modified = myStr.title()
    print(modified)
    
    
    #===========================================================================
    # Last 11 string functions
    #===========================================================================
    
    print('\n23. casefold()')
    myStr = 'This Is My String'
    modified = myStr.casefold()
    print(modified)
#     modified1 = list(reversed(modified))
#     for i in range(len(modified1)):
#         print(modified1[i], end="")
    
    
    print('\n24. expandtabs() -- Default is 8')
    myStr = 'Name\tAge\tLocation'
    print(myStr)
    print(myStr.expandtabs())
    print(myStr.expandtabs(16))
    
 
    
    print('\n25. isalnum()')
    myStr =  'Helloyou' #Space is counted as NOT alphanumeric
    myStr2 = 'Hello my friend!!'
    print('Only numbers and letters in myStr?', myStr.isalnum())
    print('Only numbers and letters in myStr2?', myStr2.isalnum())
        

    print('\n26. isalpha()')
    myStr = 'Hello'
    print('Is it only alphabetic?', myStr.isalpha())
    
    
    print('\n27. index()')
    myStr = 'Bonita High'
    print('Index for High:', myStr.index('High'))
    print('Index for High starting at 7:', myStr.index('High', 7))
#     print('Index for High starting at 8:', myStr.index('High', 8))Exception


    
    print('\n28. isdecimal()') #same as 28 isdigit()
    myStr =  'Hello' 
    myStr2 = '2020'
    print('Only numbers and letters in myStr?', myStr.isdecimal())
    print('Only numbers and letters in myStr2?', myStr2.isdecimal())
     
    
    print('\n29. isdigit()') 
    myStr =  'Hello' 
    myStr2 = '2020'
    print('Only numbers and letters in myStr?', myStr.isdigit())
    print('Only numbers and letters in myStr2?', myStr2.isdigit())
    
    
    print('\n30. isidentifier()') 
    myStr = 'Hello'
    print('Is this a variable name:', myStr.isidentifier())
#     print('Is this a variable name:', numbers.isidentifier())

    print('\n31. isprintable()') 
    s = 'Space is a printable'
    print(s)
    print(s.isprintable())
    
    s = '\nNew Line is printable'
    print(s)
    print(s.isprintable(), '\n\n')
    
    print('\n32. isspace()') 
    s = '   '
    t = 'Hello'
    print('Empty string printable?', s.isspace())
    print('Empty string printable?', t.isspace())

    print('\n32. istitle()') 
    myStr = 'I Really Like Computer Science'
    print(myStr.istitle())
    myStr = myStr.lower()
    print(myStr.istitle())
    
    