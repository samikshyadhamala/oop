#class methods
#A class method is a special kind of method (or function) that:
#Works with the class itself (the whole factory) rather than with a single toy (or object).
#It can change things about the factory (like counting how many toys have been made) or do things that affect all toys, not just one.
class Student:
    count=0
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Student.count +=1
       
       #instance methods 
    def get_info(self):
        return f"{self.name} {self.roll}"  
    #class methods
    @classmethod
    def count_no(cls):
          return f"the total no of student are={cls.count}"
    
student1=Student("samikshya",88)
student2=Student("ram",12)
print(student1.get_info())
print(Student.count_no())