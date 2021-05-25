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

# print(f'From simple calculator class: {funccalc.add(5, 5)}')
# print(f'From functional calculator class: {funccalc.method(5, 5)}')
