age=23
# txt="My name is John, I am" +age
# txt="My name is John, I am {}"
# print(txt)
# print(txt.format(age))

quantity=3
itemno=567
price=49.95
yourorder="I want {} pieces of item for {} dollars"
# yourorder="I want to pay {2} dollars for {0} pieces of item{1}"
print(yourorder.format(quantity,itemno,price))