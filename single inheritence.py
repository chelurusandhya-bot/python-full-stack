class parent:
    def display(self):
        print("this is a parent  class")
class child(parent):
    def show(self):
        print("this is a child class")
obj = child()
obj.show()
obj.display()




#multipule
class father():
    def display(self):
        print("this is a parent  class")
class mother():
    def display(self):
        print("this is a parent  class")
class child(father,mother):
    def show1(self):
        print("this is multiple inheritence")
obj = child()
obj.show1()


#multilevel
class Grandfather:
    def display(self):
        print("This is Grandfather class")

class Father(Grandfather):
    def show(self):
        print("This is Father class")

class Child(Father):
    def show1(self):
        print("This is Child class")

obj = Child()
obj.display()
obj.show()
obj.show1()









class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")

class Clothing(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display1(self):
        self.display()
        print(f"Warranty: {self.warranty} years")

c = Clothing("Shirt", 2000, 1)
c.display1()




#employee
class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")


class Programmer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def show_language(self):
        print(f"Programming Language: {self.language}")


class Developer(Programmer):
    def __init__(self, name, language, salary):
        super().__init__(name, language)
        self.salary = salary

    def show_salary(self):
        print(f"Salary: {self.salary}")


e = Developer("Sandhya", "Python", 50000)

e.display()
e.show_language()
e.show_salary()







#multiple
class Call:
    def calling(self):
        print("Calling...")

class Capture:
    def capturing(self):
        print("Capturing image...")

class Brand(Call, Capture):
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def display(self):
        print(f"Brand: {self.name}")
        print(f"Model: {self.model}")


b = Brand("Apple", "iPhone 16")


b.display()
b.calling()
b.capturing()









class student:
    def __init__(self):
        self.name = "name"
        self.__age = 12
        
    def display(self):
        print('age' ,self.__age)
s = student()
print(s.name)
s.display()
        