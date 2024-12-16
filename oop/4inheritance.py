class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eat(self):
        print(f"{self.name} is eating")
        
    def drink(self):
        print(f"{self.name} is now drinking!!!")
            
class cat(animal):
    def speak(self):
        print("meow")
   # pass#inheritance property from class animal

class dog(animal):
    def speak(self):
        print("bau bau")
    #pass

cat1=cat("okpoke",11)
dog1=dog("spooky",98)

print(cat1.name)#print cat 1 ko name 
cat1.eat()#giving cat1 access to cat then eat
dog1.speak()