# result=0
# def add(num):
#     result=0
#     result +=num
#     return result
# print(add(3))
# print(add(7))

class Result:
    def __init__(self):
        self.result=0
    def add(self,num):
        self.result+=num
        return self.result

add=Result()
print(add.add(3))
print(add.add(5))
