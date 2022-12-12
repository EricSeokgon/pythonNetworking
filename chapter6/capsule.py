class People:
    def __int__(self, age=0, name=None):
        self.__age = age
        self.name = name


p1 = People(20, 'Kim')
print(p1.name)
print(p1.__age)

