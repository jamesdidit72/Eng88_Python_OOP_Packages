# creating snake class as child class of reptile

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

# print(f'This function is from the Snake class: {snake_object.use_tongue_to_smell()}')
# print(f'This function is from the Reptile class: {snake_object.seek_heat()}')
# print(f'This function is from the Animal class: {snake_object.eat()}')
