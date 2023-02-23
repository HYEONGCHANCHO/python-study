import sys

class Person:
     def __init__(self,name,phone,addr):
          self.name=name
          self.phone=phone
          self.addr=addr
     
     def info(self):
          print("{} {} {}".format(self.name,self.phone,self.addr))


class Address:
     def __init__(self):
          self.addrList=[]
          self.fileOpen()
     
     def fileOpen(self) :
          try : file=open(r'C:\Users\a6\Desktop\web\2월4주차\day38\addressBook.csv','rt',encoding='cp949')
          except : print("파일이 없습니다")
          else:
               while True:
                    buffer=file.readline()
               # print(buffer.split(',')[0])
                    if not buffer:
                         break
                    name=buffer.split(',')[0]
                    phone=buffer.split(',')[1]
                    addr=buffer.split(',')[0].rstrip('\n')
                    self.addrList.append(Person(name,phone,addr))
               print("파일을 성공적으로 불러왔습니다.")
               file.close()

     def fileWrite(self):
          try: file=open(r'C:\Users\a6\Desktop\web\2월4주차\day38\addressBook.csv','wt',encoding='cp949')
          except : print("파일이 없습니다")
          else:
               for i in self.addrList:
                    file.write('{},{},{}\n'.format(i.name,i.phone,i.addr))
               print('파일을 수정했습니다.')
               file.close()

     def menu(self):
          # while True:
          print('\n주소록 프로그램 시작')
          print("신규 등록 1번")
          print("주소록 삭제 2번")
          print("주소록 수정 3번")
          print("주소록 검색 4번")
          print("주소록 출력 5번")
          print("프로그램 종료 0번")
          choice=int(input('번호 입력\n'))
          return choice

     def run(self):
          while True:
               choice=self.menu()
               if choice==0 : self.exit()
               elif choice==1 : self.insert()
               elif choice==2 : self.delete()
               elif choice==3 : self.update()
               elif choice==4 : self.search()
               elif choice==5 : self.printAll()
               else : print('잘못된 번호입니다.')

     def insert(self):
          name=input('추가할 이름 입력')
          phone=input('추가할 전화번호 입력')
          addr=input('추가할 주소 입력')
          if name and phone and addr:
               ask=input("추가하시겠습니까 (y/n)").upper()
               if ask != 'Y':
                    return
               self.addrList.append(Person(name,phone,addr))
          print('신규 주소록 {} {} {} 추가 완료'.format(name,phone,addr))
          self.fileWrite()

     def delete(self):
          name=input('삭제할 이름 입력')
          for i,j in enumerate(self.addrList):
               if name==self.addrList[i].name:
                    print('해당 {}의 전화 번호는 {}입니다.'.format(name,self.addrList[i].phone))
                    if input("삭제하시겠습니까 (y/n)").upper() != 'Y':
                         continue
                    self.addrList.pop(i)
                    self.fileWrite()
                    print('삭제 완료')
                    break

     def update(self):
          name=input('수정할 이름 입력')
          if not name:
               return
          updated=False
          for i,j in enumerate(self.addrList):
               if name==self.addrList[i].name:
                    print('해당 {}의 전화 번호는 {}입니다.'.format(name,self.addrList[i].phone))
                    if input("수정하시겠습니까 (y/n)").upper() != 'Y':
                         continue
                    phone=input('수정할 전화번호 입력')
                    addr=input('수정할 주소 입력')
                    self.addrList[i].phone=phone
                    self.addrList[i].addr=addr
                    self.fileWrite()
                    print('수정 완료')
                    updated=True
                    break
          if not updated:
               print('정보가 수정되지 않았습니다.')

     def search(self):
          pass

     def printAll(self):
          for i in (self.addrList):
              i.info()
          print('총 {}개의 주소록이 있습니다.'.format(len(self.addrList)))

     def exit():
          print('프로그램 종료')
          sys.exit()
          
myApp=Address()
myApp.run()
