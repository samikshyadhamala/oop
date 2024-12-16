class car:
    def __init__(self,model,year):#define constructure
        self.model=model
        self.year=year
# car1=car("bmw",2020)
# car2=car("mustang",9999)
# print(car2.model)
 #methods =action object can perform
    def drive(self):
      print(f"u need to drive {self.model}")
    
    def stop(self):
      print(f"u need to stop {self.year}")

    def describe(self):
        print(f"{self.model},{self.year}")


