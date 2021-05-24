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

# print(f'This function is from the Python class: {python_object.digest_large_prey()}')
# print(f'This function is from the Snake class: {python_object.__use_tongue_to_smell()}')  # fucntion is private, encapsulation (PILLAR 3)
# print(f'This function is from the Reptile class: {python_object.seek_heat()}')
# print(f'This function is from the Animal class: {python_object.eat()}')