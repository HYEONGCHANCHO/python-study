#__eq__메소드

class Book():
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
    
    def is_long(self):
        if self.pages >100:
            return True
        
        return False
    
    def __str__(self):
        return f"{self.title} is {self.pages} pages long"
    
    def __eq__(self,other):
        if self.title ==other.title and self.pages==other.pages:
            return True
        return False

# book1=Book("Are you My Mother?",72)
# book2=Book("The Digging dog?",72)
# print(book1==book2)

# book2=book1
# print(book1==book2)

book1=Book("Are you My Mother?",72)
book2=Book("Are you My Mother?",72)
print(book1==book2)  #False