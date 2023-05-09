from StudentManagerRepo import StudentManagerRepo

class StudentManageImpl(StudentManagerRepo):
    def __init__(self):
        self.student_list = []

    def add_student(self, student): # 학생 추가
        self.student_list.append(student)

    def list_student(self): # 전체 학생 조회
        return self.student_list

    
    def search_student(self, name): # 학생 조회
        for student in self.student_list:
            if student.name == name:
                return student
        return None

    
    def delete_student(self, name): # 학생 제거
        for student in self.student_list:
            if student.name == name:
                self.student_list.remove(student)
        return None

    
    def update_student(self, name, student): # 학생 수정
        for i, s in enumerate(self.student_list):
            if s.name == name:
                self.student_list[i] = student
                return True
        return None
