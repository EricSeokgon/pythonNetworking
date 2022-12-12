class PeoPle:
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))


class Teacher(PeoPle):
    def __init__(self, age=0, name=None, school=None):
        super().__init__(age, name)
        self.__school = school

    def showSchool(self):
        print("My school : ", self.__school)


p1 = PeoPle(29, "Lee")
p1.introMe()

t1 = Teacher(48, "Kim", "HighSchool")
t1.introMe()
t1.showSchool()
