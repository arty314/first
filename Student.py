class Student:
    def __init__(self, name, std_id, age, major, grade):
        self.__name = name
        self.__std_id = std_id
        self.__age = age
        self.__major = major
        self.__grade = grade

    def __str__(self):
        return f"이름 : {self.name} 학번 : {self.std_id} 나이 : {self.age} 전공 : {self.major} 학점 : {self.grade}"

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def std_id(self):
        return self.__std_id
    
    @std_id.setter
    def std_id(self, value):
        self.__std_id = value
    
    @property
    def age(self):
       return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value
    
    @property
    def major(self):
        return self.__major
    
    @major.setter
    def major(self, value):
        self.__major = value
    
    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        self.__grade = value