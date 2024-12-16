#parentsclass=superclass=its used within a child class to call methods from a parent class
#child class=subclass
#super()=allows u to ectend the functionality of the inherited methods

class shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    def describe(self):
        print(f"the shape color is {self.color} and {'filled' if self.filled else 'not fitted'}")
        
        
class circle(shape):
    def __init__(self,color,filled,radius):
        # self.color=color
        # self.filled=filled
        super().__init__(color,filled)
        self.radius=radius
#this is called method overwriting=if child share similar methods with parents the we will use the child version 
#so to fill this we can use super function 
    def describe(self):
        print(f"the are of circle is {3.14* self.radius * self.radius } cm^2")
        super().describe()
        
class square(shape):
    def __init__(self,color,filled,length):
        # self.color=color
        # self.filled=filled
        super().__init__(color,filled)
        self.length=length
        
class rectangle(shape):
    def __init__(self,color,filled,length,breadth):
        # self.color=color
        # self.filled=filled
        super().__init__(color,filled)
        self.length=length
        self.breadth=breadth
        

circle1=circle("red",True,55)
print(circle1.radius)
print(circle1.color)

rectangle1=rectangle("yellow",False,breadth=20,length=10)
print(rectangle1.length)
print(rectangle1.breadth)

rectangle1.describe()
circle1.describe()