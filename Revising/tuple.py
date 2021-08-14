# tuple = ("apple","banana","mango")
# x = list(tuple)
# print(type(x))
# y = ["ornage","kiwi","strawberry"]
# z = x+y
# print(z)
##################################################################################################
# list = ["apple","banana","mango"]
# for i in list:
#     print(i[0])

#################################################################################################
# fruits ={"apple":"red","banana":"yellow","apricot":"yellow"}
# fruits2 = {}
# #x= str("fruits")
# for i in fruits:
#     if i.startswith("a"):
#         x = fruits.get(i)
#         fruits2[i] = x
# print(fruits2)
#########################################################################################################
# Create a Vehicle class with max_speed and mileage instance attributes.
# #Create child class Bus that will inherit all of the variables and methods of the Vehicle class
# class Vehicle:
#     def __init__(self,max_speed,mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# v1 = Vehicle(25,30)
# print(v1.mileage)
#
# class Bus(Vehicle):
#        def __init__(self,max_speed,mileage,name):
#            self.max_speed = max_speed
#            self.mileage = mileage
#            self.name = name
#
# b1 = Bus(100,1500,"vamshi")
# print(b1.name,b1.mileage)
#########################################################################################################
# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.
#
# class Vehicle:
#     def __init__(self,max_speed,mileage,name):
#        self.max_speed = max_speed
#        self.mileage = mileage
#        self.name = name
#
#
#     def seating_capacity(self,capacity):
#         return f"the seating capcity of a{self.name} is {capacity}"
#
# class Bus(Vehicle):
#        def seating_capacity(self,capacity=50):
#           return super().seating_capacity(capacity=50)
#
# b1 = Bus(100,1500,"schoolbus")
# print(b1.seating_capacity())
##########################################################################################
# write a python class called rectangle constructed by a length and width and a method
# which will compute area of the rectangle

# class Rectangle:
#
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return (1/2)* (self.length)*(self.width)
#
# R1 = Rectangle(25,30)
# R1.area()
#
# print(R1.area())
######################################################################################
# create a parent class student and subclass School student wiht additional property subject
from typing import Tuple


# class student:
#
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#
#
# s1 = student("vamshi","krishna")
# print(s1.firstname)
#
# class school_student(student):
#
#     def __init__(self,firstname,lastname,subject):
#         student.__init__(self,firstname,lastname)
#         self.subject = subject
#     def Hello(self):
#         print("hello", self.firstname, "studying", self.subject)
#
#
# s2 = school_student("vamshi","keishna","ece")
# s2.Hello()
#
# print(s2.firstname,s2.lastname,s2.subject)
#######################################################################################################
#write a python class name called circle constructed by a radious and two methods which will compute the area and perimeter of
# a circle





class circle:
    pi = 3.14
    def __init__(self,radious):
        # self.pi = pi
        self.radious = radious


    def area(self):
        return self.pi* self.radious* self.radious


c1 = circle(25)
print(c1.area())