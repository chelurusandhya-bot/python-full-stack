class Animal:
    def eat(self):
        print("animal eat food")

class bird(Animal):
    def fly(self):
        print("bird can fly")

class parrot(bird):
    def speak(self):
        print("parrot can speak")

s = parrot()
s.eat()
s.fly()
s.speak()

#inheritence
class Camera:
    def __init__(self):
        print("Taking photo")

class MusicPlayer:
    def __init__(self):
        print("Playing music")

class SmartPhone(Camera, MusicPlayer):
    def __init__(self):
        Camera.__init__(self)
        MusicPlayer.__init__(self)
        print("Calling")

s = SmartPhone()
        







class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)   
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


e1 = Employee("Sandhya", 21, 101, 30000)

e1.display()








class Bank:
    def __init__(self):
        self.__balance = 5000   

    def show_balance(self):
        print("Balance:", self.__balance)

b = Bank()

b.show_balance()

try:
    print(b.__balance)
except AttributeError:
    print("AttributeError")


 
 


    
class Student:
    def __init__(self, name, marks):
        self.name = name      
        self.marks = marks    
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Sandhya", 95)

print("Student Name:", s1.name)
print("Student Marks:", s1.marks)

s1.display()






class wallet:
    def __init__(self):
        self .__money = 1000
    def deposit(self,amount):
        self.__money += amount
    def show_money(self):
        print("Available money:",self.__money)
w = wallet()
w.deposit(500)
w.show_money()



        
class wallet:
    def __init__(self):
        self .__money = 1000
    def withdraw(self,amount):
        self.__money += amount
    def show_money(self):
        print("Available money:",self.__money)
w = wallet()
w.withdraw(1500)
w.show_money()
        
        
        
        
        



class Wallet:
    def __init__(self):
        self.__money = 1000

    def withdraw(self, amount):
        if amount <= self.__money:
            self.__money -= amount
            print("Withdraw Successfully")
        else:
            print("Insufficient Balance")

    def show_money(self):
        print("Money Available:", self.__money)


w = Wallet()
w.withdraw(999)
w.show_money()






class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class LibraryBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)   
        self.__available = True           

    def borrow_book(self):
        if self.__available:
            print("Book Borrowed Successfully")
            self.__available = False
        else:
            print("Book is Not Available")

b1 = LibraryBook("Python Programming", "Guido van Rossum")
b1.borrow_book()
b1.borrow_book()





class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class LibraryBook(Book):
    def __init__(self, title, author):
        super().__init__(title, author)
        self.__available = True

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)

    def borrow_book(self):
        if self.__available:
            print("Book Borrowed Successfully")
            self.__available = False
        else:
            print("Book is Not Available")


b1 = LibraryBook("Central", "ABC")

b1.display_details()


b1.borrow_book()

b1.borrow_book()


