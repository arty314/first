from StudentManagerService import StudentManagerService
from Student import Student

def add_student(manager): #학생 추가
    print('새로운 학생 정보를 입력하세요.')
    name = input('이름: ')
    std_id = input('학번: ')
    age = input('나이 : ')
    major = input('전공: ')
    grade = input('학점 : ')
    student = Student(name, std_id, age, major, grade)
    manager.add_student(student)
    print('학생이 추가되었습니다.\n')

def search_student(manager): #학생 조회
    print('검색할 학생 이름을 입력하세요.')
    name = input('이름: ')
    student = manager.search_student(name)
    if not student:
        print('해당하는 학생이 없습니다.\n')
    else:
        print(student)
        print('')

def list_student(manager): #전체 학생 조회
    print('전체 학생 목록을 조회합니다.')
    student = manager.list_student()
    for i, student in enumerate(student):
        print(f'{i + 1}. {student}')

def delete_student(manager): #학생 제거
    print('삭제할 학생 이름을 입력하세요.')
    name = input('이름: ')
    student = manager.search_student(name)
    if not name:
        print('해당 이름의 학생은 등록되어있지 않습니다. \n')
    else:
        manager.delete_student(name)
        print('학생이 삭제되었습니다.\n')

def update_student(manager): #학생 수정
    print('수정할 학생 정보를 입력하세요.')
    name = input('이름: ')
    student = manager.search_student(name)
    if not student:
        print('해당하는 학생이 없습니다.\n')
    else:
        print(f'<현재 {name} 학생의 정보> {student}')
        new_name = input('변경할 이름 (변경하지 않으려면 엔터): ')
        new_std_id = input('변경할 학번 (변경하지 않으려면 엔터): ')
        new_age = input('변경할 나이 (변경하지 않으려면 엔터): ')
        new_major = input('변경할 전공 (변경하지 않으려면 엔터): ')
        new_grade = input('변경할 성적 (변경하지 않으려면 엔터): ')

        if new_name:
            student.name = new_name
        if new_std_id:
            student.std_id = new_std_id
        if new_age:
            student.age = new_age
        if new_major:
            student.major = new_major
        if new_grade:
            student.grade = new_grade
        manager.update_student(name, student)
        print('학생 정보가 수정되었습니다.\n')


def main(manager):
    while True:
        print("===============")
        print("1. 학생 추가")
        print("2. 학생 검색")
        print("3. 전체 학생 조회")
        print("4. 학생 제거")
        print("5. 학생 수정")
        print("6. 종료")
        print("===============")
        option = int(input())
        if option == 1:
            add_student(manager)
        elif option == 2:
            search_student(manager)
        elif option == 3:
            list_student(manager)
        elif option == 4:
            delete_student(manager)
        elif option == 5:
            update_student(manager)
        elif option == 6:
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == '__main__':
    manager = StudentManagerService()
main(manager)
