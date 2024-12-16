#classvariable=shared among all the instances of a class,define outside the constructor,allow u to share data among all the objects created from that class
#instances=object created from a class=objects
#instance variable=variable that are defined within a class and are unique to each instance(object) of that class
class student:
    graduate_year=2028
    no_of_student=0
    def __init__(self,name,age):#name and class are  
        self.name=name
        self.age=age
        student.no_of_student +=1
        
student1=student("samikshya",11)
student2=student("ram",88)
student3=student("sparsha",99)
st=student("akj",87)#calling the same class so count 

# print(student1.name)
# print(student1.age)
# print(student1.graduate_year)#call by object created from class
# print(student.graduate_year)#call from the name of the class itself
print(student.no_of_student)
print(f"hello i am {student1.name} .my age is {student1.age} and i graduate from {student1.graduate_year} with {student.no_of_student} no of students.")