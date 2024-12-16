#polymorphism=many form
#2 ways to achieve polymorphism
#1.inheritance=object could be treated of the same type as a parents
#2.duck typing

#1 =we can also use abstract method here
class shape:
    
    def area(self):
        pass
    
class circle(shape):
    
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        print(f"hte area is {3.14 *self.radius **2 }")  
          
class rectangle(shape):
    
     def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth 
        
     def area(self):
        print(f"the area is { self.length * self.breadth }")    
       
class triangle(shape):
    def __init__(self,base,height):
        self.height=height
        self.base=base
    
    def area(self):
        print(f"the are is { self.height * self.base *0.5 }") 
        
# class pizza():
#     def __init__(self,topping,radius):
#         self.topping=topping
#         self.radius=radius
 #since pizza doesnot inheritance from the shape class
  
class pizza(circle):
    def __init__(self,topping,radius):
        self.topping=topping
        super().__init__(radius)
        
           
shapes=[circle(1),rectangle(2,2),triangle(3,4),pizza("pineapple",22)]

# shapes=[circle(1),rectangle(2,2),triangle(3,4)]


# tr=triangle(2,2)
# tr.area()

for i in shapes:
    i.area()