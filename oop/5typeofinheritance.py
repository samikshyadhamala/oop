#multiple inheritance= inherit from more than one parent class
#multilevel inheritance=inheritance from a parent which inherit from another parents

#multilevel inheritance
class animal:
    def __init__(self,name):
        self.name=name
        
    def sleep(self):
        print("this animal is sleeping")
    def dance(self):
        print(f"{self.name} is dancing")
#multiple inheritance
class prey(animal):
    def eats(self):
        print("u are gonna be dead")
class hunter(animal):
    def hunt(self):
        print("i am gonna eat u")

class rabbit(prey):
    pass
class lion(hunter):
    pass
class snake(prey,hunter):
    pass

rab1=rabbit("scouby")
lion1=lion("roar")
snake1=snake("hiss")

rab1.eats()
snake1.hunt()
lion1.hunt()
rab1.dance()