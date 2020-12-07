'''
ogracias
Current Module: chapter3.RealWorldFunctionsUsingPython
Date: Nov 7, 2020
AP Computer Science Principles
Periods 1, 3
'''


# imports(such as math)
# functions(All your functions should be added here independent of when they 
# are used in your client code below
# Taxi fare -----------------------------------------------
def metertoKm(m):
    return m / 1000

def meterToMiles(m):
    miles = (m / 1000) * 0.621371
    return miles

def rate140Meters(m):
    units = m / 140;
    amountDue = units * 0.25
    return amountDue

# Recycling -------------------------------------
def smallBottles(num):
    recycleSmall = num * 0.1
    return recycleSmall

def largeBottles(num):
    recycleSmall = num * 0.25
    return recycleSmall

# Shipping fees ---------------------------------
def shipping():
    firstItemPrice = 11
    itemsShipped = int(input('How many items are you shipping? '))
    expeditedItems = int(input('How many items are being expedited? '))
    subtotal_itemsShipped = ((itemsShipped - 1) - expeditedItems)
    subtotal_itemsShipped *= 3
    subtotal_itemsExpedited = expeditedItems * 15.00
    print('\nFirst item subtotal: ${:,.2f}'.format(firstItemPrice))
    print('Items shipped: ${:,.2f}'.format(subtotal_itemsShipped))
    print('Expedited items: ${:,.2f}'.format(subtotal_itemsExpedited))
    all3Combined = firstItemPrice + subtotal_itemsShipped + subtotal_itemsExpedited
    print('\nYour subtotal is: ${:,.2f}'.format(all3Combined))
    taxTotal = all3Combined * 0.08
    print('Added tax at 8%: ${:,.2f}'.format(taxTotal))
    print('Your total is: ${:,.2f}'.format(all3Combined + taxTotal))


# main here
if __name__ == '__main__': 
    print('###################   Question #1  ###################')
    print(' -- Welcome to Spain -- ')
    meters = float(input('Enter amount of meters traveled: '))
    print('You have travelled', round(meterToMiles(meters), 2), 'miles, or',
           metertoKm(meters), 'km')
    print('Your total is: ', '${:,.2f}'.format(rate140Meters(meters)))
    '''
    In a particular jurisdiction in Spain, taxi fares consist of a base 
    fare of $4.00, plus $0.25 for every 140 meters traveled. 
    Write function(s) that take the distance traveled (in meters) as 
    its only parameter and return the total fare as its only result, 
    and convert the meters to miles within the function, 
    [1 km --> 0.621371 miles] and display both the 
    amount of kilometers and its conversion to the user, plus the total 
    amount due. (American travelers like to see this conversion in European 
    or Latin American countries)
    
    Format the output so that it includes a dollar sign, and
    
    The result should always display two decimal places.
    
    Add the correct docString to this function
    '''
    
    
    print('\n\n###################   Question #2  ################### ')
    less1lt = int(input('How many container <= 1L do you have?'))
    more1lt = int(input('How many container >= 1L do you have?'))
    returnedSmall = smallBottles(less1lt)
    returnedLarge = largeBottles(more1lt)
    print('\nYour refund for <= 1L bottles is: ${:,.2f}'.format(smallBottles(less1lt)))
    print('Your refund for >= 1L bottles is: ${:,.2f}'.format(largeBottles(more1lt)))
     
    print('\nYour total is: ${:,.2f}'.format(returnedSmall + returnedLarge))
    ###################   Question #2  ################### 
    '''
    In many jurisdictions a small deposit is added to drink containers to
     encourage people to recycle them. In one particular jurisdiction, 
     drink containers holding one liter or less have a $0.10 deposit, 
     and drink containers holding more than one liter have a $0.25 deposit.
     
     Write a program that reads:
    1. The number of containers of each size from the user ( 1L or less and over 1 L)
    
    2. Your program should continue by computing and displaying the refund 
       that will be received for returning each of those containers volumes. 
       ( Less than 1 liter, and 1 liter and above)
    
    3. Format the output so that it includes a dollar sign, and
    
    4. The result should always display two decimal places.
    
    **** Add the correct docString to this function
    
    '''
    
    print('\n\n###################   Question #3  ################### ')
    shipping()
#     firstItemPrice = 11
#     itemsShipped = int(input('How many items are you shipping? '))
#     expeditedItems = int(input('How many items are being expedited? '))
#     subtotal_itemsShipped = ((itemsShipped - 1) - expeditedItems)
#     subtotal_itemsShipped *= 3
#     subtotal_itemsExpedited = expeditedItems * 15.00
#     print('\nFirst item subtotal: ${:,.2f}'.format(firstItemPrice))
#     print('Items shipped: ${:,.2f}'.format(subtotal_itemsShipped))
#     print('Expedited items: ${:,.2f}'.format(subtotal_itemsExpedited))
#     all3Combined = firstItemPrice + subtotal_itemsShipped + subtotal_itemsExpedited
#     print('\nYour subtotal is: ${:,.2f}'.format(all3Combined))
#     taxTotal = all3Combined * 0.08
#     print('Added tax at 8%: ${:,.2f}'.format(taxTotal))
#     print('Your total is: ${:,.2f}'.format(all3Combined + taxTotal))
    ###################   Question #3  ################### 
    '''
    Write a program which provides an online retailer shipping fees at these
    rates:
    a) The first item is $11.00
    b) Any subsequent items  will be $3.00 each
    c) Any 'expedited' items will cost $15.00
    Develop a program which will ask the user how many items are being shipped,
    and how many are expedited items. (only 2 questions should be asked)
    d) The program should provide a subtotal at this point.
    e) The program should add a tax of 8.00% 
    f) Finally, it should also provide a total amount, and thank the user 
    for using its services.
    
    Format the output so that it includes a dollar sign, and
    The result should always display two decimal places.
    
    '''