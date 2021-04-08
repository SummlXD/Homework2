class CallMixin():

    def call(self):
        print (f"calling to {self.fname} {self.lname} on {self.phone}")

class Person(CallMixin):

    def __init__(self,fname,lname,phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone

    def info(self):
        return "omegalul"
brian = Person("Brian","Steinkamp","0101")

brian.call()





