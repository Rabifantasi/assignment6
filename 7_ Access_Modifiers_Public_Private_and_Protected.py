# Create a class Employee with:

#a public variable name,

#a protected variable _salary, and

#a private variable __ssn.

#Try accessing all three variables from an object of the class and document what happens.

class Employ:

    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn         # Private variable

emp= Employ("Rabia", 100000, 123456789)

print(emp.name)

print(emp._salary)

print(emp.__ssn) 

print(emp._Employ__ssn)
