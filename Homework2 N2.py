class Animal():
    def __init__(self, saxeli, asaki, **kwargs):
        super().__init__(**kwargs)
        self.saxeli = saxeli
        self.asaki = asaki

    def info(self):
        return f"sxeli: {self.saxeli}, asaki: {self.asaki}" \
 \
                def get_saxeli(self):

            return self.saxeli

    def set_name(self):
        self.saxeli = saxeli

    def get_asaki(self):
        return self.asaki

    def set_asaki(self):
        self.asaki = asaki


class Dog(Animal):
    def __init__(self, saxeli, asaki, jishi, feri):
        super().__init__(saxeli, asaki)
        self.jishi = jishi
        self.feri = feri

    def info(self):
        return Animal.info(self) + "jishi: {self.jishi}, feri = {self.feri}"


gigi = Dog("giorgi", 20, "riot", "lurji")

print(gigi.info())














