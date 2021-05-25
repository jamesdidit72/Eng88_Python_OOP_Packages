from functional_calc import Function_Calc

class Input_Calc(Function_Calc):
    def __init__(self):  # function that sets the values
        # a keyword called SUPER which inherits everything from parent class (Animal)at the time of initialisation of this class
        super().__init__()

    def inputted_value(self):
        self.value_1 = int(input("Enter a value:  "))
        self.value_2 = int(input("Enter another value:  "))
        input_calc.select_method()

    def select_method(self):
        active = True
        while active:
            operator = input('Enter either +, -, *, /, % or inch:  ')
            if operator == '+':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.add(self.value_1, self.value_2)}')
            elif operator == '-':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.subtract(self.value_1, self.value_2)}')
            if operator == '*':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.multiply(self.value_1, self.value_2)}')
            elif operator == '/':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.divide(self.value_1, self.value_2)}')
            if operator == '%':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.method(self.value_1, self.value_2)}')
            elif operator == 'inch':
                print(f'{self.value_1} {operator} {self.value_2} = {input_calc.inch(self.value_1)}')
        else:
            print('failed')


input_calc = Input_Calc()

input_calc.inputted_value()
