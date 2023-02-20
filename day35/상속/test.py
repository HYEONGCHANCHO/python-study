#사옥
class Employee:
    interest=1.02
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    def fullname(self):
        print(f"{self.first} {self.last}")
    
    def sallay(self):
        self.sallay=int(self.pay*self.interest)
        return self.sallay

class Developer(Employee):
    interest=1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

# class Manager(Employee):
#     def __init__(self,first,last,pay,employee=None):
 
    
#     def add_emp(self,emp):
   
#     def print_emp(self):
      
#     def remove_emp(self,emp):
      

em1=Employee('Kim','Smith',5000)
em2=Employee('Park','John',6000)
em3=Developer('Ru','Jane',7000,'python')
em4=Developer('cho','may',7500,'java')

print(em1.fullname())
print(em2.fullname())
print(em3.fullname())
print(em4.fullname())
print(em1.sallay())
print(em2.sallay())
print(em3.sallay())
print(em4.sallay())
