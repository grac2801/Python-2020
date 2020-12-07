
#Date: Dec 2, 2020
#ogracias
#Current Module: chapter8.lists
#AP Computer Science Principles

#imports, variables, CONSTANTS




#functions



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
    print('----- find the index -----')
    print(marxes.index('Raphael'))
    is_here = 'Rachel' in marxes
    print('Rachel found in marxes: ', is_here)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    