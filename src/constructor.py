class laptop:
    def __init__(self,name):
        print("laptop details")
        self.name=name
        self.price=""
    def display(self):
        print(self.name)
        print(self.price)
Hp=laptop("Hp")
Hp.price=60000
Hp.display()
##
class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def __init__(self,a,b):
        print(a**b)
c1=calculator(10,2)
print(c1.add(10,20))
print(c1.sub(3,2))
print(c1.mul(3,3))




