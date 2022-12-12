class People:
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))


class Teacher(People):
    def __init__(self, age=0, name=None, school=None):
        super()._init__(age, name)
        self.__school = school


    def introMe(self):
        super().introMe()
        print("School : ", self.__school)


class Student(Teacher):
    def __int__(self, age=0, name=None, school=None, grade=None):
        super().__int__(age, name, school)
        self.__grade = grade

    def introMe(self):
        super().introMe()
        print("Grade : ", self.__grade)


p1 = People(29, "Lee")
p1.introMe()

t1 = Teacher(48, "Kim", "HighSchool")
t1.introMe()

s1 = Student(17, "Park", "HighSchool", 2)
s1.introMe()
