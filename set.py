class Calculator:
    def add(self, a=0, b=0, c=0):
       return a + b + c
calc = Calculator()
print("Add 1 value (10):", calc.add(10))
print("Add 2 values (10, 20):", calc.add(10, 20))
print("Add 3 values (10, 20, 30):", calc.add(10, 20, 30))
