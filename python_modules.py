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

#print(random())
# what is the use case
#

from random import random
import math

number = random()
print(number)
if number < 0.49999:
    print(math.floor(number))
else:
    print(math.ceil(number))





