class FourCal:
    # def setdata(self,first,second):
    #     self.first=first
    #     self.second =second
    def __init__(self,first,second):
        self.first=first
        self.second=second
        self.result=0

    def add(self):
        result=self.first+self.second
        return result
    
    def mul(self):
        result=self.first*self.second
        return result
    
    def sub(self):
        result=self.first-self.second
        return result
    
    def div(self):
        result=self.first/self.second
        return result

a=FourCal(1,2)
# a.setdata(1,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
    