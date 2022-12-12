class People:
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name = name


p1 = People(20, "Kim")
print(p1.getName())
print(p1.getAge())
