# Python OOP
## Four pillars of OOP
- Abstraction
  - Hiding unnecessary data, such as when importing modules or looking up the PC specs, it doesn't tell us how it's done, just the answer
- Inheritance
  - Inherit data from another class, such as how a database extracts data from different databases
- Encapsulation
  - When you need to restrict access, such as a bank account. _age = 22 means the variable is private
- Polymorphism
    - Once code has been inherited from another class, you can change, add new etc without effecting the parent class that the data code was taken from

### Packages
#### Modules
- keyword for implementing these modules is 'import'
- import random  standard way of calling  module
```python
import random
from random import random
```
#### Using modules for maths
- if the value is 1.49 floor() will return 1, value of 1.54 ceil() returns 2
```python
from random import random
import math
number = random()
print(number)
if number >= 0.5:
    print(math.ceil(number))
else:
    print(math.floor(number))
```
#### os, sys are used to get information about your localhost/ your machine such as name, path etc
```python
import os, sys, datetime, math

print(os.cpu_count())
print(datetime.datetime.today())
print(math.remainder(1, 5))
def current_system_path():
    print(f'This is your current path:')
    return sys.path


def working_directory():
    print(f'This is your current working directory:')
    return os.getcwd()


print(current_system_path())
print(working_directory())
```
#### further math work
```python
import math
print(math.pi)
```

### The four pillars example
- Each class is on a different file
#### Animal (Parent class, uses Abstraction)
```python
class Animal:
    def __init__(self):  # self refers to this class
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True
    def breath(self):
        return 'Breathe to stay alive'
    def eat(self):
        return 'Eat, you need food'
    def reproduce(self):
        return 'Find yourself a partner'
    def move(self):
        return 'Walk like an Egyptian'
# create an object of our Animal class
# without making a object, you cannot call the class
cat = Animal()  # creating an object from the animal class called cat
print(cat.move())  # moving for cat is abstracted (PILLAR 1)
```
#### Reptile class (Inheritance)
```python
from animal import Animal  # imports the parent class 

class Reptile(Animal):
    def __init__(self):
        # a keyword called SUPER which inherits everything from parent class (Animal)at the time of initialisation of this class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = 0
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        return 'Its getting cold, seek some heat'
    def hunt(self):
        return 'Hunt for food'
    def use_vemon(self):
        return 'Reptile uses Vemon attack'
    def attract_male_through_scent(self):
        return 'use scent to attract a partner'

reptile_object = Reptile()

print(f'From animal class: {reptile_object.eat()}')
print(f'From reptile class: {reptile_object.use_vemon()}')
# This is the amazing benefit of using OOP with inheritance (PILLAR 2)
```
#### Snake class
```python
from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        # a keyword called SUPER which inherits everything from parent class (Animal)at the time of initialisation of this class
        super().__init__()
        self.cold_blooded = True
        self.forked_tongue = True
        self.vemon = None
        self.limbs = False

    def __use_tongue_to_smell(self):
        return 'I can smell how you taste... '


snake_object = Snake()

print(f'This function is from the Snake class: {snake_object.use_tongue_to_smell()}')
print(f'This function is from the Reptile class: {snake_object.seek_heat()}')
print(f'This function is from the Animal class: {snake_object.eat()}')
```
#### Python class (Encapsulation and polymorphism)
```python
from snake import Snake

class Python(Snake):
    def __init__(self):
        # a keyword called SUPER which inherits everything from parent class (Animal)at the time of initialisation of this class
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.vemon = False

    def digest_large_prey(self):
        return 'Delicious prey...'
    def constrict(self):
        return 'So tight'
    def climb(self):
        return 'One speedy boi'
    def shed_skin(self):
        return 'New year, new me'


python_object = Python()
dog_object = Python()
print(dog_object.eat())  # polymorphism (PILLAR 4)

print(f'This function is from the Python class: {python_object.digest_large_prey()}')
print(f'This function is from the Snake class: {python_object.__use_tongue_to_smell()}')  # function is private, encapsulation (PILLAR 3)
print(f'This function is from the Reptile class: {python_object.seek_heat()}')
print(f'This function is from the Animal class: {python_object.eat()}')
```
# Important for OOP code
- All classes after the parent class require:
  - from 'previous_file_name' import 'previous_class_name'
  - def __init__(self):
  - super().__init__()
- Requires an object for the class to be called from
### Simple calculator
```python
class Calculator:  # initialisation of the class
    def add(self, value_1, value_2):  # add function
        return value_1 + value_2

    def subtract(self, value_1, value_2):  # subtract function
        return value_1 - value_2

    def multiply(self, value_1, value_2):  # multiply function
        return value_1 * value_2

    def divide(self, value_1, value_2):  # divide function
        return value_1 / value_2
mycalc = Calculator()  # sets class to a variable
```
### Functional calculator
```python
from OOP_calc_task import Calculator


class Function_Calc(Calculator):
    def __init__(self):  # function that sets the values
        # a keyword called SUPER which inherits everything from parent class (Animal)at the time of initialisation of this class
        super().__init__()
        self.value_1 = 0
        self.value_2 = 0

    def method(self, value_1, value_2):  # divisible function
        if value_2 == 0:
            return False
        elif value_1 % value_2 == 0:  # if the value_1 can be divided by the value_2 with no remainder, then return True
            return True
        else:
            return False

    def triangle(self, height, base):  # area of a triangle function
        return (height * base) / 2

    def inch(self, value_1):
        return value_1 * 2.54  # multiplies the value by the length of an inch in centimeters
funccalc = Function_Calc()
```
### Input calculator
```python
from functional_calc import Function_Calc

class Input_Calc(Function_Calc):
    def __init__(self):  # function that sets the values
        # a keyword called SUPER which inherits everything from parent class (Animal)at the time of initialisation of this class
        super().__init__()

    def continue_calc(self):
        keep_calculating = input("Do you want to continue? Y/N:  ")  # collects value from user
        if keep_calculating.upper() == 'N':
            print('happy calculating!')
        else:
            input_calc.inputted_value()

    def inputted_value(self):
        self.value_1 = int(input("Enter a value:  "))  # collects value from user
        self.value_2 = int(input("Enter another value:  "))  # collects value from user
        input_calc.select_method()  # runs the select method

    def select_method(self):
        active = True
        while active:  # while True, do this:
            operator = input('Enter either +, -, *, /, % or inch, or "exit" to leave:  ')  # collects operator from user
            if operator == '+':  # checks what the input is
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.add(self.value_1, self.value_2)}')
                active = False
            elif operator == '-':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.subtract(self.value_1, self.value_2)}')
                active = False
            elif operator == '*':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.multiply(self.value_1, self.value_2)}')
                active = False
            elif operator == '/':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.divide(self.value_1, self.value_2)}')
                active = False
            if operator == '%':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.method(self.value_1, self.value_2)}')
                active = False
            elif operator.lower() == 'inch':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.inch(self.value_1)}')
                active = False
            elif operator.lower() == 'exit':
                print('exiting...')
                active = False
        else:
            print('I hope you got your answer')
            input_calc.continue_calc()


input_calc = Input_Calc()

input_calc.inputted_value()
```