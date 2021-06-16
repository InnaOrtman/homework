# Task 1
# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student, and another one called Teacher.
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not.
# For example, the name should be a Person attribute, while salary should only be available to the teacher.

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return f'Person: {self.name}, {self.surname}, {self.age} years old'


class Student:
    def __init__(self, surname, age):
        self.surname = surname
        self.age = age

    def __repr__(self):
        return f'Person: {self.surname}, {self.age} years old'


class Teacher(Student):
     def __init__(self, surname, age):
         self.surname = surname
         self.age = age

     def salary(self, experience):
        self.experience = experience
        self.salary = self.experience * self.age / 100 * 4200
        return f'The teacher`s salary is: {self.salary}'


jane = Person('jane', 'robson', 23)
joan = Teacher('havruliv', 56)
jack = Student('levko', 32)
print(jane)
print(joan)
print(joan.salary(6))
print(jack)
