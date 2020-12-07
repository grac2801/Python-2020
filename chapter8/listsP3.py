
#Date: Dec 2, 2020
#ogracias
#Current Module: chapter8.lists
#AP Computer Science Principles

#imports, variables, CONSTANTS




#functions
def removeLastItem(L):
    '''
    (list) --> list
    Removes last item in the list
    [1,2,3,4] --> [1,2,3]
    '''
    del L[-1]
    return L



if __name__ == "__main__":
    print()
    print('----- Syntax of a list -----')
    weekDays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    print(weekDays)
    print(type(weekDays))
    
    print()
    print('----- Combined lists -----')
    big_birds = ['emu', 'ostrich', 'cassowary']
    first_Names = ['Sebastian', 'Danielle', 'Anne']
    combined = [weekDays, big_birds, first_Names]
    print(combined)
    
    print('First list only:', combined[0])
    print('list 2 item 2:', combined[1][1])
    
    
    print()
    print('----- offsets -----')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Mario']
    print(marxes)
    print(marxes[4], ' = ', marxes[-1])
    # list[beg : end(exclusive)]
    print(marxes[1:4])
    
    
    print()
    print('----- Change items in a list -----')
    print(marxes)
    marxes[2] = 'Aaron'
    print(marxes)
    # list[beg : end(exclusive) : step]
    print('Using colon:', marxes[:])
    print('Using colon:', marxes[::2])
    print('using negative: ', marxes[::-1])
    
    
    print()
    print('----- append() -----')
    appendedList = [1, 2, 3]
    marxes.append('Raphael')
    print(marxes)
    
    print()
    print('----- extend() -----')
    extendedvalues = ['extended1', 'extended2']
    print(extendedvalues)
    marxes.extend(extendedvalues)
    print(marxes)
    
    print()
    print('----- concatenation -----')
    others = ['Gummo', 'Karl']
    marxes += others
    print(marxes)
    
    print()
    print('----- insert() -----')
    marxes.insert(3, 'first')
    print(marxes)
    
    print()
    print('----- remove() -----')
    marxes.remove('extended1')
    marxes.remove('extended2')
    print(marxes)

    
    print()
    print('----- pop() -----')
    #The default for pop is last item of the list
    marxes.pop()
    print(marxes)
    marxes.pop(0)
    print(marxes)
    
    print()
    print('\n\n----- find the index -----')
    print(marxes.index('Raphael'))
    is_here = 'Rachel' in marxes
    print('Rachel found in marxes: ', is_here)
    print('marxes:', marxes)
    
    
    print('\n\n----- join() -----')
    separator = ', '
    print(separator.join(marxes))
    
    print('\n\n----- sorted() -----')
    #Make a copy of your list
    sortedMarxes = sorted(marxes)
    print(sortedMarxes)
    marxes[0] = 'original'
    print('marxes:', marxes)
    print('sortedMarxes:', sortedMarxes)
    
    
    
    
    print('\n\n----- sort -----')
    print(marxes)
    marxes.pop(0)
    print(marxes)
    
    #sorting to original list
    marxes.sort(reverse=True)
    print('using sort:', marxes)
    
    numbers = [2, 1, 6.7, 34, 0.1]
    numbers.sort(reverse=False)
    print(numbers)
    
    
    
    print('\n\n----- Make a function call using a list -----')
    print(removeLastItem(numbers))
    
    
    print('\n\n----- Make a new list and aliases -----')
    a = [1, 2, 3]
    print('a:', a)
    b = a[:] #Creating a new list independent of original one
    print('b:', b)
    print('id for a', id(a))
    print('id for b', id(b))
    a[0] = 1000
    print('a:', a)
    print('b:', b)
    
    c = list()
    print(c)
    c.append(123)
    print(c)
    d = list()
    d += [12, 24, 36]
    e = []
    e.extend(d)
    print(d)
    print(e)
    
    print('\n\n----- built-ins -----')
    randomNumbers = [34, 23, 67, 89, 12]
    emptylist = []
    print(max(randomNumbers))
    print(min(randomNumbers))
    print(sum(randomNumbers))
    print(any(emptylist))
    print(chr(177))
    print(len(randomNumbers))
    
    print('updated')
    
    
    
    
    