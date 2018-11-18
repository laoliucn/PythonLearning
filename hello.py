'''# Add two numbers
num1 = 3
num2 = 5
sum = num1+num2
print(sum)

print("Hello World!")

def double(num):
    """Function to double the value"""
    return 2*num

print(double.__doc__)
print(double(3))'''

"""a,b,c = 1, 2.3, 5+6j
print(a, "is of type", type(a))
print(b, "is of type", type(b))
print(c, "is of type", type(c))

print(c, "is complex number?", isinstance(c,complex))

s = '''multiline string
second line
third line'''
print(s)

myTuple = (3, 2, "5", 9, 7)
print(myTuple)

mySet = {3, 2, "5", 9, 7}

print(mySet)

x = 12.3456789
print('The value of x is %8.2f' %x)

import sys

for path in sys.path:
	print(path)"""


# def greet(name):
# 	"""This function greets to
# 	the person passed in as
# 	parameter"""
# 	print("Hello, " + name + ". Good morning!")
# 	print("Hello, " , name , ". Good morning!")

# greet("Travis")


# # Program to double each item in a list using map()

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# new_list = list(map(lambda x: x * 2 , my_list))

# # Output: [2, 10, 8, 12, 16, 22, 6, 24]
# print(new_list)

# with open("test.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")

# import os
# print(os.getcwd())
# a = 2
# print(id(2))
# print(id(a))

# sides = [0 for i in range(5)]
# print(type(sides))

# sides = list(range(5))
# print(sides)

# class Celsius:
#     def __init__(self, temperature = 0):
#         self._temperature = temperature

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

#     @property
#     def temperature(self):
#         print("Getting value")
#         return self._temperature

#     @temperature.setter
#     def temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("Setting value")
#         self._temperature = value


# myTemp = Celsius(20)
# print(myTemp.temperature)
# myTemp.temperature = 37
# print(myTemp.temperature)
# print(myTemp._temperature)

class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    def print_stu(self):
        print('name:%s, score:%s' % (self.__name, self.__score))

    def hello(self):
        print('name:%s, score:%s' % (self.name, self.score))


a = Student('Travis', 98)
a.print_stu()
a.hello()
