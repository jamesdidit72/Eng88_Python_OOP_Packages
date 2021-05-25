# creating a reptile class to inherit everything from animal class

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

# print(f'From animal class: {reptile_object.eat()}')
# print(f'From reptile class: {reptile_object.use_vemon()}')
# This is the amazing benefit of using OOP with inheritance (PILLAR 2)
