# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person's name is {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher subject is: {self.subject}")

teacher1 = Teacher("Rabia", "Python")
teacher2 = Teacher("Ali", "Java")
teacher3 = Teacher("Sara", "C++")




