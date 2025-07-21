# class - class is blueprint of object == first word shoukd be capital 
# object - is isnstanece of class == called usning class 

""" syntax - class classname:
                def method(self):
                    content

            my_car = classname()
            my_car.method() """

"""
class Bike:
    def start(self):
        print("Woom. Woom.")

honda = Bike()
honda.start()
"""

# Attributes = variables that belong to a class or object.
# Methods = functions inside a class that define the behavior of objects.

class Student :
    school = "ABC high school"

    def __init__(self, name , age):
        self.name = name
        self.age = age

    def show_detail(self):
        print(f"The name of student is {self.name} and he is {self.age} year old ")

s1 = Student("Rohan",20)

s1.show_detail()