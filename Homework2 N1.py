class Book():
    def __init__(self,saxeli,avtori,gamoshvebis_weli):
        self._saxeli = saxeli
        self.__avtori = avtori
        self.__gamoshvebis_weli = gamoshvebis_weli
    
    def info(self):
        return f"wignis saxeli :{self._saxeli}, avtori :{self.__avtori}, gamoshvebis weli :{self.__gamoshvebis_weli}"\

wigni = Book("raghac","vighac","0000")
print(wigni.info())
















