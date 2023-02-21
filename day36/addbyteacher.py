# addressbook
import sys
class Person:
    def __init__(self,name,phone,addr):
        self.name = name
        self.phone = phone
        self.addr = addr
    def info(self):
        print('{} {} {}'.format(self.name,self.phone,self.addr))
class AddressBook:
    def __init__(self):
        self.address_list = []
        self.file_reader()
    def file_reader(self):
        try:
            file = open('addressBook.csv','rt')
        except: # 없으면
            print('해당 파일이 없습니다.')
        else: # 있으면
            while True:
                buffer = file.readline() # 이때 버퍼는 긴 한줄의 문장으로 읽어온다
                if not buffer:  # 버퍼에 없으면
                    break   # 빠져나가고
                name = buffer.split(',')[0] # 읽어온 버퍼를 ,로 나눈 첫번째 값을 name에 넣어준다.
                phone = buffer.split(',')[1]
                addr = buffer.split(',')[2].rstrip('\n') # 읽어온 버퍼를 ,로 나눈 세번째 값을 addr에 넣어주고, 줄바꿈을 추가해준다.
                self.address_list.append(Person(name,phone,addr))
            print('파일을 읽었습니다.')
            file.close()

    def file_generator(self):
        try:
            file = open('addressBook.csv', 'wt') 
        except:
            print('addressBook.csv 파일을 생성할 수 없습니다.')
        else:
            for person in self.address_list:
                file.write('{}  {}  {}\n'.format(person.name, person.phone, person.addr))
            file.close()




    def menu():
        print("-"*30)
        print('신규 주소록 등록은 1번')
        print('기존 주소록 삭제는 2번')
        print('기존 주소록 수정은 3번')
        print('주소록 검색은 4번')
        print('전체 주소록 출력은 5번')
        print('프로그램 종료는 0번')
        print("-"*30)
        choice = int(input('원하는 메뉴를 선택하세요'))
        return choice
    def exit(self):
        print('프로그램을 종료합니다')
        sys.exit()
    def run(self):
        while True:
            choice = AddressBook.menu()
            if choice == 0: self.exit()
            elif choice == 1 : self.insert()
            elif choice == 2 : self.delete()
            elif choice == 3 : self.update()
            elif choice == 4 : self.search()
            elif choice == 5 : self.printAll()
            else : print('잘못된 선택입니다.')
    def insert(self):
        print("== 새로운 연락처를 생성합니다 ===")
        name =input('등록할 이름:')
        phone =input('등록할 전화번호:')
        addr = input('등록할 주소:')

        if name and phone and addr:
            self.address_list.append(Person(name,phone, addr))
            self.file_generator()
            print('새로운 주소가 만들어졌습니다')
        else:
            print('입력이 잘못되어 주소록이 만들어지지 않았습니다')



    def delete(self):
        print("==기존 주소를 삭제 ==")
        name =input('삭제할 이름입력')
        if not name: 
            print('입력한 이름이 없어서 삭제할 수 없습니다')
            return
        deleted = False
        for i,person in enumerate(self.address_list):
            if name == self.address_list[i].name:
                print('검색된 전화번호는 {}'.format(self.address_list[i].phone))
                if input('정말로 삭제하시겠습니까 (Y/N)').upper() != 'Y':
                    continue
                self.address_list.pop(i)
                deleted =True
                print('{}의 정보를 삭제했습니다'.format(name))
                self.file_generator()
                break
        if not deleted:
            print('{}의 정보가 삭제되지 않았습니다'.format(name))




# 특정내용을 A가 가지고 있다가 B줄때 
# enumerate()는 인덱스번호와 내용을 모두 가져온다

    def update(self):
        print("==기존 정보 수정 ==")
        name = input('수정할 이름 입력')
        if not name:
            print('이름이 없어 취소합니다')
            return
        
        updated = False
        for i, person in  self.address_list:
            if name== self.address_list[i].name:
                print('검색되 전화번호 "{}" 입니다'.format(self.address_list[i].phone))
                if input('수정할까요(Y/N) :').upper() !='Y':
                    continue
                new_phone = input('변경할 전화번호 입력:')
                if new_phone:
                    self.address_list[i].phone = new_phone
                
                new_addr=input('변경할 주소입력')
                if new_addr:
                    self.address_list[i].addr= new_addr

                updated=True
                print('주소록이 수정되었습니다')
                self.address_list[i].info()
                self.file_generator()
                break

        if not updated:
            print('{}의 정보가 수정되지 않았습니다'.format(name))   


    def search(self):
        print('==주소록 검색==')
        name =input('찾을 이름을 입력')
        if not name:
            print('입력된 이름이 없습니다')
            return
        exist = False

        for person in self.address_list:
            if name == person.name:
                person.info()
                exist=True
        if not exist:
            print("{}의 정보를 찾을 수 없습니다".format(name))
        

    def printAll(self):
        print("==전체 연락처 ==")    
        for person in self.address_list:
            person.info()

        print('총 {}개의 주소록이 있습니다'.format(len(self.address_list)))


myapp = AddressBook()
myapp.run()









