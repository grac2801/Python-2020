'''
Created on Nov 18, 2020

@author: ogracias
'''

print()
print('----- If statements -----')
'''
pH level        Category
0 - 4           Strong acid
5 - 6           Weak acid
7               Neutral
8 - 9           weak base
10-14           Strong base
'''
pH = float(input('Enter the pH level: '))
if pH < 7.0:
    print('\nIt is acidic!')
    print('You should be careful with that!!')
if pH > 7.0:
    print('It is basic!!')
if pH == 7:
    print('It is neutral!!')
#     
print()
print('----- Start of: Nested if statements -----')
value = input('Enter the pH level: ')
if len(value) > 0:
    pH = float(value)
if pH < 7.0:
    print('\nIt is acidic!')
    print('You should be careful with that!!')
if pH > 7.0:
    print('It is basic!!')
if pH == 7:
    print('It is neutral!!')
  
  
print()
print('----- if and grades -----')
grade =  float(input('Enter your percent grade: '))
if grade > 90:
    print('You have an A')
if grade > 80:
    print('You have a B')
if grade > 70:
    print('You have a C')
if grade > 60:
    print('You have a D')
  

grade =  float(input('\nEnter your percent grade: '))
if grade > 90:
    print('You have an A')
elif grade > 80:
    print('You have a B')
elif grade > 70:
    print('You have a C')
elif grade > 60:
    print('You have a D')
print('End of grade checking')


print()
print('----- Else keyword -----')
compound = input('Enter the compound: ')
if  (compound == 'H2O') or (compound =='h2o'):
    print('Water')
elif  compound == 'NH3':
    print('Ammonia')
elif  compound == 'CH4':
    print('Methane')
else:
    print('I don\'t know which compound this is')






















      