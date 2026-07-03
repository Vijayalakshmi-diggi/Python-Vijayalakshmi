#single inheritance
class animal:
    def speak(self):
        print("animals cannot speak")
class dog(animal):
    def bark(self):
        print("animals can bark")
d=dog()
d.bark()
d.speak()

#multiple Inheritance
class dad:
    def phone(self):
        print("dad's phone")
class mom:
    def laptop(self):
        print("mom's laptop")
class son(dad,mom):
    def school(self):
        print("son goes to scholl")
s1=son()
s1.phone()
s1.laptop()
s1.school()
#multilevel 
class Grandpa:
    def quality(self):
        print("wisdom")
class parents(Grandpa):
    def quality2(self):
        print("Discipline")
class child(parents):
    def quality3(self):
        print("creativity")
son=child()
son.quality()
son.quality2()
son.quality3()

dad=parents()
dad.quality()
dad.quality2()
#dad.quality3() --> cannot cal 

#hierarchical 
class dad:
    def money(self):
        print("dad'd money")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass 
s1=son1()
s1.money()
s2=son2()
s2.money()
# super()
class Grandpa:
    def quality(self):
        print("wisdom")
class parents(Grandpa):
    def quality(self):
        super().quality()
        print("Discipline")
#takes left side parameter for super()
class child(parents,Grandpa):
    def quality(self):
        super().quality()
        print("creativity")

s1=child()
s1.quality()

