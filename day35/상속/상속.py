class Employee:
    interest=1.02
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    def sallary(self):
        self.pay=int(self.pay*self.interest)
        return self.pay
class Developer(Employee):
    interest=1.10
    def __init__(self,first,last,pay,pro_lang):
        super().__init__(first,last,pay)
        self.pro_lang=pro_lang
class Manager(Employee):
    def __init__(self, first, last, pay,employee=None):
        super().__init__(first, last, pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee
    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)
    def print_emp(self):
        for emp in self.employee:
            print("매니저는",emp.fullname())
    def remove_emp(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)


em1=Employee('Kim','Smith',5000)
em2=Employee('Park','John',6000)
em3=Developer('Ru','Jane',7000,'python')
em4=Developer('cho','may',7500,'java')

print(em1.fullname())
print(em2.fullname())
print(em3.fullname())
print(em4.fullname())
print(em1.sallary())
print(em2.sallary())
print(em3.sallary())
print(em4.sallary())

man1=Manager("Yoon",'Sae',12000)
print(man1.fullname())
print(man1.sallary())

man1.add_emp(em1)
man1.print_emp()
man1.remove_emp(em1)
man1.add_emp(em2)
man1.print_emp()