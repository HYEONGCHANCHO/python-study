# class Add:
#     def result(self,x,y):
#         print("Addition",x+y)
# class Multi:
#     def result(self,x,y):
#         print("Multiplication",x*y)

# m=Multi()
# m.result(10,20)

# a=Add()
# a.result(10,20)
class Add:
    def result(self,x,y):
        print("Addition",x+y)
class Multi(Add):
    def result(self,x,y):
        super().result(x,y)
        print("Multiplication",x*y)

m=Multi()
m.result(10,20)
