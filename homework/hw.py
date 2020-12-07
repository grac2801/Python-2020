
#Date: Dec 5, 2020
#ogracias
#Current Module: homework.hw
#AP Computer Science Principles

#imports, variables, CONSTANTS




#functions
def different(a, b):
    answer = a != b
    return answer

if __name__ == '__main__':
#     print()
#     print('----- 6 -----')
#     print(different(5, 6))
#     print(5 > 6)
# 
#     print('\n\n----- 7a -----')
#     population = 2562
#     land_area = 1000
#     if population < 10000:
#         print(population)
#         
#         
#     print('\n\n----- 8 -----')
#     pH = float(input('Enter pH: '))
#     if pH < 3:
#         print(pH, 'is very acidic! Be careful')
#     elif pH < 14:
#         print(pH, 'is acidic!')
    age = int(input('Enter age:'))
    bmi = int(input('What is your bmi? '))
    
    if age < 45:
        if bmi < 22.0:
            shape = 'light'
        else:
            shape = 'heavy'
    else:
        if bmi < 22:
            risk = 'medium'
        else:
            risk = 'high'
            
    print(risk)
    
    
    
    
    
    
    
    
    