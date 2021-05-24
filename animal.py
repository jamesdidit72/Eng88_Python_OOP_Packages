# animal file to create Animal class
# use pass to run when its empty

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


# cat = Animal()  # creating an object from the animal class called cat
#
# print(cat.move())  # moving for cat is abstracted (PILLAR 1)
