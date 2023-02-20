#사옥
class Employee:
    interest=1.02
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def sallay(self):
        self.pay=int(self.pay*self.interest)
        return self.pay

class Developer(Employee):
    interest=1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employee=None):
        super().__init__(first,last,pay)
        if employee is None:
            self.employee=[]
        else :
            self.employee=employee
    
    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)
    
    def print_emp(self):
        for emp in self.employee:
            print("---> ", emp.fullname())

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
print(em1.sallay())
print(em2.sallay())
print(em3.sallay())
print(em4.sallay())

man1=Manager("Yoon","Sae",12000)
print(man1.fullname())
print(man1.sallay())

man1.print_emp()
print("매니저 추가")
man1.add_emp(em2)
man1.print_emp()
man1.add_emp(em3)
man1.print_emp()
print("매니저 삭제")
man1.remove_emp(em2)
man1.print_emp()
print("is sub class?")
print(issubclass(Manager,Developer))   #왼쪽이 오른쪽의 상속을 받았는가?
print(issubclass(Developer,Employee))