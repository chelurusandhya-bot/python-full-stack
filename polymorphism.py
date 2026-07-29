#methodoverriden #polymorphism

class animal:
    def sound(self):
        print("animal sound")
        
class Dog(animal):
    def sound(self):
        print("Bark")
        
class Cat(animal):
    def sound(self):
        print("Meow")
        
d = Dog()
c = Cat()


d.sound()
c.sound()

#ducktype

class Dog:
    def sound(self):
        print("Bark")
        
class Cat:
    def sound(self):
        print("Meow")
def make_sound(animal):
    animal.sound()
make_sound(Dog())
make_sound(Cat())
        


#overriding

class cal:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
obj = cal() 
print(obj.add(10,20,30))     
    
    
    
    
#overloading
class cal:
    def add(self,a,b,c=0,d=0):
        return a+b+c+d
obj = cal() 
print(obj.add(10,20,30))






#Abstraction with abstraction

from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class rectangle(shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print(self.l*self.b)
r = rectangle(2,3)
r.area()
        
        
        
from abc import ABC,abstractmethod

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print(0.5 * self.b * self.h)

t = Triangle(4, 6)
t.area()







from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
        self.pi = 3.14

    def area(self):
        print( self.pi * self.r * self.r)

c = Circle(2)
c.area()



#with out abstraction

class shape():
    def area(self):
        print("area method")
    
class rectangle(shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print(self.l*self.b)
r = rectangle(2,3)
r.area()


class vehical:
    def run(self):
        print("vehical is running")
        
class bus(vehical):
    def run(self):
        print("bus is going")
        
class car(vehical):
    def run(self):
        print("car have 4 wheels")
        
b = bus()
c = car()


b.run()
c.run()




import modules
print(modules.add(10,20))
        





