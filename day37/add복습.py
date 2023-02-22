import sys

class Person:
    def __init__(self,name,phone,addr):
        self.name=name
        self.phone=phone
        self.addr=addr

    def info(self):
        print("{} {} {}".format(self.name,self.phone,self.addr))

#개인별 정보 Person 클래스 종료=======================================

class AddressBook:
    def __init__(self):
        self.address_list=[]
        self.file_reader()

    def file_reader(self):
        try:
            file=open(r'C:\web\addressBook.csv','r')
        except:
            print('파일이 없습니다.')
        else:
            while True:
                buffer=file.readline()
                if not buffer:
                    break
                name=buffer.split(',')[0]
                phone=buffer.split(',')[1]
                addr=buffer.split(',')[2].rstrip('\n')
                self.address_list.append(Person(name,phone,addr))

        print('파일의 내용을 모두 읽었습니다')
        file.close()

    def menu(self):
        print("===메뉴===")
        print('신규 주소록 등록은 1번')
        print('기존 주소록 삭제는 2번')
        print('기존 주소록 수정은 3번')
        print('주소록 검색은 4번')
        print('전체 주소록 출력은 5번')
        print('프로그램 종료는 0번')
        choice=int(input("수행할 작업을 선택"))
        return choice

    def file_generator(self):
        try:
            file=open('addressBook.csv','wt')
        except:
            print('addressBook.csv 파일을 생성할 수 없습니다')
        else:
            for person in self.address_list:
                file.write('{}, {}, {}\n'.format(person.name,person.phone,person.addr))
            file.close()

    def run(self): #첫화면에는 메뉴목록이 와야함
        while True: #메뉴출력, 메뉴에서 선택
            choice=AddressBook.menu(self)
            if choice==0: self.exit()
            elif choice==1: self.insert()
            elif choice==2: self.delete()
            elif choice==3: self.update()
            elif choice==4: self.search()
            elif choice==5: self.printAll()
            else:print('없는 명령입니다')

    def exit(self):
        print('프로그램을 종료합니다')
        sys.exit()

    def insert(self):
        print("== 새로운 연락처를 생성합니다 ===")
        name =input('등록할 이름:')
        phone =input('등록할 전화번호:')
        addr = input('등록할 주소:')
        if name and phone and addr:
            self.address_list.append(Person(name,phone,addr))
            print('새 주소가 정삭적으로 등록되었습니다.')
            self.file_generator()
        else:
            print('새 주소가 등록되지 않았습니다.')

    def delete(self):
        print("==기존 주소를 삭제 ==")
        name =input('삭제할 이름입력')

        if not name:
            print('입력된 이름이 없습니다.')
            return

        deleted=False
        for i,person in enumerate(self.address_list):
            if name==self.address_list[i].name:
                print('검색된 전화번호가 "{}"입니다'.format(self.address_list[i].phone))
                if input('정말로 삭제하시겠습니까? (Y/N)').upper() !='Y':
                    continue

                self.address_list.pop(i)
                deleted=True
                print('{}의 정보를 삭제했습니다'.format(name))
                self.file_generator()
                break
        
        if not deleted:
            print('{}의 정보가 삭제되지 않았습니다'.format(name))

    def update(self):
        print("==기존 정보 수정 ==")
        name = input('수정할 이름 입력')
        if not name:
            print('이름이 없어 취소합니다')
            return
        updated=False
        for i,person in enumerate(self.address_list):
            if name==self.address_list[i].name:
                print('검색된 전화번호가 "{}"입니다.'.format(self.address_list[i].phone))
                if input('수정할까요? (y/n) >>>').upper() != 'Y':
                    continue
                new_phone=input('변경할 전화번호를 입력하세요')
                if new_phone:
                    self.address_list[i].phone=new_phone
                new_addr=input('변경할 주소를 입력하세요')
                if new_addr:
                    self.address_list[i].addr=new_addr
                updated=True
                print('주소록이 수정되었습니다. 수정된 주소록의 내용을 확인하세요')
                self.address_list[i].info()
                self.file_generator()
                break

        if not updated:
            print('{}의 정보가 수정되지 않았습니다.'.format(name))

    def search(self):
        print('==주소록 검색==')
        name =input('찾을 이름을 입력')
        if not name:
            print('입력된 이름이 없습니다')
            return
        exist = False
        for person in self.address_list:
            if name==person.name:
                person.info()
                exist = True
        if not exist:
            print('{}의 정보가 없습니다'.format(name))

    def printAll(self):
        print("==전체 연락처 ==")    
        for person in self.address_list:
            person.info()
        print('총 {}개의 주소록이 있습니다'.format(len(self.address_list)))
    
#AddressBook 클래스 종료 =============================================

myapp=AddressBook()
myapp.run() #run 메소드를 만들어서 실행
