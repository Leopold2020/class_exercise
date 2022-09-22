#Oskar Svedlund
#TEINF-20
#2022-09-22
#klass ovning

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def change_name(self):
        self.name = input("New name\n>> ")

    
class Student(Person):
    def __init__(self, name, gender, age, classes : list):
        super().__init__(name, gender, age)

        self.classes = classes


class Teacher(Person):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)

class classes:
    def __init__(self, name, students : list):
        self.name = name
        self.students = students
        

class course:
    def __init__(self, name, students : list, teachers : list, assignment : list):
        self.name = name
        self.students = students
        self.teachers = teachers
        self.assignment = assignment

