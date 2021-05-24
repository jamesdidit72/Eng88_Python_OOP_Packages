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
### Snake class
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
### Python class (Encapsulaion and polymorphism)
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
print(f'This function is from the Snake class: {python_object.__use_tongue_to_smell()}')  # fucntion is private, encapsulation (PILLAR 3)
print(f'This function is from the Reptile class: {python_object.seek_heat()}')
print(f'This function is from the Animal class: {python_object.eat()}')
```