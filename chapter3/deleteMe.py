'''
Created on Nov 10, 2020

@author: ogracias
'''
def shippingTotal(s, e):
    '''
    (float, float) --> float, float, float
    It takes the first parameter and takes second parameter
    and returns expedited and subsequent item prices and subtotal
    finally adding 8% tax
    (10, 2) --> $62.00, $4.96, $66.96
    '''
    return (((s - 1) * 3.00) + (e * 15.00) + 11.00)


sub = float(input('How many items are you shipping? '))
exp = float(input(' How many items are being expedited? '))
subTotal = shippingTotal(sub, exp)
tax = (0.08 * subTotal)
total = tax + subTotal
print('Your subtotal is: ${:,.2f} ' .format(subTotal))
print('Added tax of 8%: ${:,.2f}' .format(tax))
print('Your total is: ${:,.2f} ' .format(total))