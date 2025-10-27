class Employe:
    Salary = 234
    increment = 20

    @property
    def salarybefore_increment(self):
        return (self.Salary + self.Salary * self.increment / 100)
    
    @salarybefore_increment.setter
    def salaryafter_increment(self,salary): 
       self.increment = ((salary/self.Salary)-1) * 100

e = Employe()
e.salaryafter_increment = 300

print(e.increment)