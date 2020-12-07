
#Date: Nov 22, 2020
#ogracias
#Current Module: chapter6.scienceEquationsLibrary
#AP Computer Science Principles

#imports, variables, constants

GAS_CONSTANT = 0.0821


#functions
def force(m, a):
    return m * a

def idealGasLaw_getMol(atm, lit, Kelvin):  
    pv = atm * lit
    rt = GAS_CONSTANT * Kelvin
    n = pv / rt
    return round(n, 2)

#===============================================================================
# complete the other 2 functions
#===============================================================================