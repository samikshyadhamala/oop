#polymorphism types
#if it look like a duck and quack like a duck then it must be duck
#objects must have a minimumnecessary attributes/methods
class animal:
    alive=True
    
class dog(animal):
    def speak(self):
        print("vau vau")
        
class cat(animal):
    def speak(self):
        print("meow") 
        
class car:#satisfy the minimum conditions
    alive=False
    # def horn(self):
    def speak(self):
        print("honk")      
 
#attribue error=animals=[dog(),cat(),car()]
animals=[dog(),cat(),car()]
# cat1=cat()
# print(cat1.alive)
for i in animals:
       i.speak()
       print(i.alive)