
#Date: Nov 22, 2020
#ogracias
#Current Module: chapter6.importedTempLibrary
#AP Computer Science Principles

#imports
import chapter6.echo as e
import chapter6.F2temperatureLibrary as T
from chapter6 import F2temperatureLibrary
# from chapter6.F2temperatureLibrary import aboveFreezing, convertToCelsius
# from chapter6 import F2temperatureLibrary
# from chapter6.F2temperatureLibrary import aboveFreezing
# from chapter6.F2temperatureLibrary import *



#functions



if __name__ == "__main__":
    print(T.aboveFreezing(83.5))
    print('F1_Imported: ', __name__)
#     print(aboveFreezing(83.3))
#     print(aboveFreezing(83.3))
    print('F2_Library:', F2temperatureLibrary.__name__)
    print('echo import:', e.__name__)