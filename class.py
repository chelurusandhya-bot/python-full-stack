class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        self.course= course
    def display(self):
        print(f'Name:{self.name},Age: {self.age}')
s= student('sandy',22)
s.display()








class Student:
    def __init__(self, name, course, phone):
        self.name = name
        self.course = course
        self.phone = phone

    def display(self):
        print(f"Name: {self.name}, Course: {self.course}, Phone: {self.phone}")

    def study(self):
        print(f"{self.name} is studying {self.course}")

s = Student("Sandhya", "Python FSD", 8523865723)

s.display()
s.study()





class Student:
    def __init__(self, name, course, phone):
        self.name = name
        self.course = course
        self.phone = phone

    def display(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")
        print(f"Phone: {self.phone}")

s = Student("Sandy", "Python", 8523865723)
s.display()