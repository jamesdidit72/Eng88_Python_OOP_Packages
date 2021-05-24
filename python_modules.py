# what are python modules
# We have built in modules that we can find on Pythons library
# if the value is 1.49 floor() will return 1, value of 1.54 ceil() returns 2
# keyword for implementing these modules is 'import'

# import random  standard way of calling  module
from random import random
#  module name     function name
import math
# num1 = 23.66
# #print(num1)
# print(math.ceil(num1))
# print(math.floor(num1))

# number = random()
# print(number)
# if number >= 0.5:
#     print(math.ceil(number))
# else:
#     print(math.floor(number))

# os, sys are used to get information about your localhost/ your machine such as name, path etc

import os, sys
# working_directory = os.getcwd()
# print(f'This is your current working directory: {working_directory}')
#
# system_path = sys.path
# print(f'This is your current path: {system_path}')

def current_system_path():
    print(f'This is your current path:')
    return sys.path

def working_directory():
    print(f'This is your current working directory:')
    return os.getcwd()


print(current_system_path())
print(working_directory())
