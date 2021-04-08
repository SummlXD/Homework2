class Animal():
    def __init__(self, saxeli, asaki):

        self._saxeli = saxeli
        self.__asaki = asaki

    def info(self):
        return f"sxeli: {self._saxeli}, asaki: {self.__asaki},"\

    def get_saxeli(self):
        return self._saxeli

    def set_name(self,saxeli):
        self._saxeli = saxeli

    def get_asaki(self):
        return self.__asaki

    def set_asaki(self,asaki):
        self.__asaki = asaki


class Dog(Animal):
    def __init__(self, saxeli, asaki, jishi, feri):
        super().__init__(saxeli, asaki)
        self._jishi = jishi
        self.__feri = feri

    def info(self):
        return Animal.info(self) + f" jishi: {self._jishi}, feri = {self.__feri}"


dobby = Dog("dobby", 20, "ver verkvevi dzaghlebis jishebshi", "lurji")

print(dobby.info())








