
#Date: Nov 22, 2020
#ogracias
#Current Module: chapter6.scienceEquations
#AP Computer Science Principles

#imports
import chapter6.scienceEquationsLibrary as lib



#functions



if __name__ == "__main__":
    #===========================================================================
    # Interface
    #===========================================================================
    

    userInput =   int(input( '''
print('Which formula do you wish to use?')
Enter 1 \u2192 \'force equation\'
Enter 2 \u2192 \'ideal gas law\'
Enter 3 \u2192 \'gravitational force\'
Enter 4 \u2192 \'specific heat\'')
     '''  )) 
    
    #===========================================================================
    # Decision making to re-route user to desired equation
    #===========================================================================
    if userInput == 1:
        print('--Force equation algorithm--')
        mass = float(input('Enter mass: '))
        acc = float(input('Enter acceleration: '))
        print(lib.force(mass, acc))
    elif userInput == 2:
        print('--Ideal Gas Law algorithm--')
        pressure = float(input('Enter pressure in atm: '))
        volume = float(input('Enter volume in liters: '))
        temperature = float(input('Enter temperature in \u00B0K: '))
        moles = lib.idealGasLaw_getMol(pressure, volume, temperature)
        print('Your moles:', moles)
    #========================================================================
    # Continue with program
    #========================================================================
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
