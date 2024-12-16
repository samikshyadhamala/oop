#static methods=a methods that belongs to a class rather than any objects from the class (instance)
#best for utility function that do not need access to class data
#instance methods=belong to individual objects best for opertaion on instances

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
        
    def output(self):
        return f"{self.name}={self.position}"
    
    @staticmethod
    def valid_position(position):
        return position in ("manager","dj","cook","receptionist","sweeper")
    
worker1=Employee("ram","manager")
worker2=Employee("hari","dj")
worker3=Employee("fin","janitor")

print(worker1.name)
#static method =u oinly need to call the classes no need to create any object from the class
print(Employee.valid_position("jnaitor"))
#instance methods=access the objects then tcall the instance methods
print(worker1.output())
print(worker2.output())
print(worker3.output())