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