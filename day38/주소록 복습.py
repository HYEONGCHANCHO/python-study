import sys

class Person:
     def __init__(self,name,phone,addr):
          self.name=name
          self.phone=phone
          self.addr=addr
     
     def info(self):
          print("{},{},{}".format(self.name,self.phone,self.addr))
     
#class Person의 끝=====================================================       

class AddressBook:
     def __init__(self):
          self.address_List=[]  #전역변수처럼 사용하기 위해 적어줌
          self.file_reader()

     #파일 불러오기
     def file_reader(self):
          try: file=open(r'C:\Users\a6\Desktop\web\2월4주차\day38\addressBook.csv','rt')
          except: print('파일이 없습니다.')
          else: 
               while True:
                    buffer=file.readline()
                    if not buffer:
                         break
                    name=buffer.split(',')[0]
                    phone=buffer.split(',')[1]
                    addr=buffer.split(',')[2].rstrip('\n')
                    #읽어온 정보를 어딘가에 저장 각 사람의 정보를 세트로 저장해주려면 class를 사용해야함
                    self.address_List.append(Person(name,phone,addr))                    
               print('파일을 모두 읽었습니다')
               file.close()

     #파일 자체를 수정
     def file_write(self):
          try:file=open(r'C:\Users\a6\Desktop\web\2월4주차\day38\addressBook.csv','wt')
          except:print('파일에 저장할 수 없습니다.')
          else: 
               for person in self.address_List:
                    file.write('{},{},{}'.format(person.name,person.phone,person.addr))
               file.close()

     # #메뉴고르기
     def menu():
          print("신규회원 등록 1번")
          print("기존회원 삭제 2번")
          print("기존회원 수정 3번")
          print("주소록 검색 4번")
          print("전체주소록 출력 5번")
          print("프로그램 종료 0번")
          choice=int(input('수행할 작업을 선택하세요'))
          return choice

     #menu()를 불러서 실행하는 함수
     def run(self):
          while True:
               choice=AddressBook.menu()
               if choice==0: exit() 
               elif choice==1:self.insert()
               elif choice==2:self.delete()
               elif choice==3:self.update()
               elif choice==4:self.search()
               elif choice==5:self.printAll()
               else: print('잘못된 선택입니다.')

     #신규회원 가입
     def insert(self):
          print('==새로운 주소록을 생성합니다.==')
          name=input("등록할 이름 입력")
          phone=input("등록할 전화번호 입력")
          addr=input("등록할 주소 입력")

          #입력받을 때 name입력이 안되면 검색에 문제가 발생함, 값 3개가 모두 입력되었을 때만 저장하도록함.
          if name and phone and addr:
               self.address_List.append(Person(name,phone,addr))
               print('신규 회원이 정상적으로 등록되었습니다.')
          else : 
               print("정보가 누락되어 저장할 수 없습니다.")

          self.file_write()

     #기존회원 삭제
     def delete(self):
          print('==기존 주소록에서 삭제합니다.==')
          name=input("삭제할 이름을 입력하세요")
          if not name:
               print("입력된 이름이 없어서 삭제를 취소합니다.")
               return
          deleted=False    
          for i,person in enumerate(self.address_List): 
               if name==self.address_List[i].name:
                    print('검색된 전화번호가 {}입니다'.format(self.address_List[i].phone))
                    if input('삭제하시겠습니까(y/n)').upper() != 'Y':
                         continue
                    self.address_List.pop(i)
                    print('{}의 정보를 삭제했습니다.'.format(name))
                    deleted=True
                    self.file_write()
                    break
          if not deleted:
               print("{}의 정보를 삭제할 수 없습니다.".format(name))

     #기존회원 내용 수정
     def update(self):
          print('==기존 회원의 내용을 수정합니다.==')
          name=input('수정할 이름 입력')
          if not name:
               print("입력된 이름이 없어 수정을 취소합니다.")
               return
          updated=False
          for i,person in enumerate(self.address_List):
               if name==self.address_List[i].name:
                    print("검색된 전화번호는 {}입니다.".format(self.address_List[i].phone))
                    if input('정말 수정하시겠습니까? (y/n)').upper() != 'Y':
                         continue
                    new_phone=input('변경할 전화번호 입력')
                    if new_phone:
                         self.address_List[i].phone=new_phone
                         print(i)
                    new_addr=input('변경할 주소 입력')
                    if new_addr:
                         self.address_List[i].addr=new_addr
                         print(i)
                    updated=True
                    self.address_List[i].info()
                    print('주소록이 수정되었습니다.')

                    self.file_write()
                    break
          if not updated:
               print('{}정보가 수정되지 않았습니다.'.format(name))

     #기존회원 찾기, 이름으로 찾기
     def search(self):
          print('==주소록을 검색합니다.==')
          name=input('찾을 이름을 입력')
          if not name:
               print('입력된 이름이 없어 검색을 취소합니다.')
               return
          exist=False
          for person in self.address_List:
               if name==person.name:
                    person.info()
                    exist=True
          if not exist:
               print("{}의 정보가 없습니다".format(name))
          
     #기존회원 전체를 출력
     def printAll(self):
          print('==주소록 전체를 출력합니다.==')
          for person in self.address_List:
               person.info()
          print('총 {}개의 주소록이 있습니다'.format(len(self.address_List)))

     #프로그램 종료
     def exit(self):
          print('프로그램을 종료합니다')
          sys.exit()

#class AddressBook의 끝=====================================================       

#실행문
myapp=AddressBook()
myapp.run()












