#composition=this composed objects directly owns its components,which cannot wxist independently "owns-a" relationship
#aggregation=It means that one object can contain or hold other objects, but the contained objects can also exist independently.
#composition=A house is made of rooms. If the house is destroyed, the rooms no longer exist in the same way. The rooms are parts of the house, so they depend on the house.
class engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower
        
class wheel:
    def __init__(self,radius):
        self.radius=radius
        
class car:
    def __init__(self,name,year,horsepower,radius):
        self.name=name
        self.year=year
        self.engine_pp=engine(horsepower)
        self.wheel4=wheel(radius)
        
    def display(self):
        print(f"{self.name} {self.year} {self.engine_pp.horsepower} {self.wheel4.radius}")
car1=car("bmw",2020,78,90)

car1.display()    
        #if we deltet