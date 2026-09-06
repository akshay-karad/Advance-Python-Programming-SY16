class Employee:
    raise_amount = 1.05
    def __init__(self,name,salary):
        self.name = name
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount 
Employee.set_raise_amount(1.10)
print(Employee.raise_amount)   
