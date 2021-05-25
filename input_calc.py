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
                print(f'{self.value_1} in {operator}/s  = {input_calc.inch(self.value_1)}')
                active = False
            elif operator.lower() == 'exit':
                print('exiting...')
                active = False
        else:
            print('I hope you got your answer')
            input_calc.continue_calc()


input_calc = Input_Calc()

input_calc.inputted_value()
