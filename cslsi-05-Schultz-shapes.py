# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:01:19 2017

@author: Bruce
"""

class Shape:
    def __init__(self, x=0, y=0, color=None):
        self.x = x
        self.y = y
        self.color = color
        
    def translate(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        
    def position(self):
        return (self.x, self.y)
    
    def get_color(self):
        return self.color
        
    def set_color(self, color):
        self.color = color
        
class Rectangle(Shape):
    def __init__(self,x=0, y=0, color=None, width=1, height=1):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height
    
    def circumference(self):
        return 2*self.width + 2*self.height
    
class Square(Rectangle):
    def __init__(self,x=0, y=0, color=None, length=1):
        self.width = length
        self.height = length
        super().__init__(x, y, color)

class Triangle(Shape):
    def __init__(self, x=0, y=0, color=None, sidea=1, sideb=1, sidec=1):
        self.sidea = sidea
        self.sideb = sideb
        self.sidec = sidec
        super().__init__(x, y, color)
        
    def area(self):
        s = 0.5*(self.sidea + self.sideb + self.sidec) #Heron's Formula
        return (s*(s-self.sidea)*(s-self.sideb)*(s-self.sidec))**0.5
    
    def circumference(self):
        return self.sidea + self.sideb + self.sidec

class Ellipse(Shape):
    def __init__(self,x=0, y=0, color=None, a=1, b=1):
        self.a = a
        self.b = b
        super().__init__(x, y, color)
    
    def area(self):
        return 3.14*self.a*self.b
    
    def circumference(self):
        return (2*3.14)*(((self.a**2+self.b**2)/2)**0.5)
    
class Circle(Ellipse):
    def __init__(self, x=0, y=0, color=None, r=1):
        self.a = r
        self.b = r
        super().__init__(x, y, color)
    
    def circumference(self):
        return 2*3.14*self.a


rec = Rectangle(x=1, y=5, color='grey', width=2, height=4)
sqr = Square(x=-3, y=4, color='black', length=3)
tri = Triangle(x=0, y=9, color='red', sidea = 5, sideb = 3, sidec = 4)
ell = Ellipse(x=1, y=5, color='blue', a=2, b=4)
cir = Circle(x=-7, y=1, color='purple', r=4)

shapes = [rec, sqr, tri, ell, cir]

for shape in shapes:
    print(shape.__class__.__name__, "\n"+"Shape's initial position:", shape.position())
    shape.translate(2, 3)
    print("Shape's new position after translation:", shape.position(), "\n\n"+\
          "Area of shape:", shape.area(), "\n"+\
          "Perimeter/Circumference of Shape:", shape.circumference(), "\n\n"+ \
          "Initial color of shape:", shape.get_color())
    shape.set_color('rainbow')
    print("New color of shape:", shape.get_color(),     "\n\n")
