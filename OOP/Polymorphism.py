#Two diff class have the same method name , u cam call then with any object from those classes
#without worrying about which one is which

class Cat:
    def speak(self):
        return "I am cat"

class Dog:
    def speak(self):
        return "i am dog"

animal = [Dog(), Cat()]
print(animal[0].speak())
print(animal[1].speak())

for animal in animal:
    print(animal.speak())
    print(animal.speak())

class Clock:
    def tick(self):
        print("tick-tock ")

class Time:
    def tick(self):
        print("tick am time")

c1 = [Clock(), Time()]
print(c1[0].tick())
print(c1[1].tick())

for obj in c1:
    print(obj.tick())
    print(obj.tick())
