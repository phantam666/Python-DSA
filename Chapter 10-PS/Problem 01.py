class Programmer:
    Company = "Google"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary    

p = Programmer("John", 30, 100000)
print(p.name, p.age, p.salary)  # Output: John