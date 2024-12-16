#nested class=a class defined within another class
#benifits=allows u to logically group classes that are closelty related
#encapsulates private details that arenot relevant outside of the other outer class
#keeps the namespace clean;reduces the posibility of naming conflicts

# class employe:
#     print("first emplyee")
# class employe:
#     print("second employe")
#to avoid such nameing challenge
class company:
    def __init__(self,company_name):
        self.company_name=company_name
        self.employee_list=[]
        
        
    class employee:
        def __init__(self,name,position):
           self.name=name
           self.position=position
           
        def get_details(self):
            return f"{self.name} {self.position}"

    
    def add_employee(self,name,position):
           new_employee=self.employee(name,position)
           self.employee_list.append(new_employee)
           
    def loop(self):
        return [employee.get_details() for employee in self.employee_list]
    
company1=company("kfc")
# employee1=company.employee("ram","manager")
# employee2=company.employee("sam","tech")
# employee2=company.employee("broom","machine")
company1.add_employee("ram","oop")
company1.add_employee("shy","lol")
company1.add_employee("hi","ok")
# print(company1.company_name)
# print(employee1.name)
# print(employee1.get_details())
print(company1.loop())
