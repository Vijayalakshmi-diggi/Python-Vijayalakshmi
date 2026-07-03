#operator polymorphism
print(1+6)
# concatination for string
print("hello" + "world")
#joins two list 
print([1,2]+[3,4])
# * is also polymorphic
print(5*2)
print("hi"*3)

#method overriding 
class animal:
    def sound(self):
        print("some sound")
class Dog(animal):
    def sound(self):
        print("dog barks")
d=Dog()
d.sound()
# duck typing
class dog:
    def speak(self):
        print("barks")
class cat:
    def speak(self):
        print("meow")
def animal_sound(animal):
    animal.speak()
d=dog()
c=cat()
animal_sound(d)
animal_sound(c)
#function polymorphism
print(len("Python"))               
print(len([10, 20, 30]))         
print(len((1, 2, 3, 4)))            

print(max(10, 20, 30))           
print(max("Apple"))   
