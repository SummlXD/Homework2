class Mylist():
    def __init__(self,data):
        self.data = data

    def __str__(self):
        return  f"{self.data}"\

    def __add__(self, other):
        added_data = self.data + other.data
        return Mylist(added_data)

    def __mul__(self, other):
        multied_data = self.data * other
        return Mylist(multied_data)

l1 = Mylist([1,2,3])
l2 = Mylist([6,7])
h = Mylist(2)

print((l1*2).data)
print((l1+l2).data)
print(str(l1))















