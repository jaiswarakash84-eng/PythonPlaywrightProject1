# Inheritance allow a "child" class to drive attribute and methods from the "parent" class
#this helps u avoid repeacted code

#single level inheritance

# class animal:
#     def breath(self):
#         print("animal breath")
#
# class dog(animal):
#     def bark(self):
#         print("dog bark")
#
# d1 = dog()
# d1.breath()
# d1.bark()

class Car:
    def start(self):
        print("start the car")

    def stop(self):
        print("stop the car")

class Bike(Car):
    def __init__(self, brand):
        self.brand = brand

b1 = Bike("Honda")
b1.start()
b1.stop()
print(b1.brand)

#Multiilevel

class A:
    def method(self):
        print("method of A")

    def method2(self):
        print("method2 of A")

class B(A):
    def __init__(self, name):
        self.name = name

class C(B):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

c1 = C("Akax", 27)
print(c1.age)
print(c1.name)
print(c1.method())
print(c1.method2())

