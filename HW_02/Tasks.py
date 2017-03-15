'''
Created on Mar 14, 2017
@author: vodachuk
'''
from math import *
x = input("x = ")
y = input("y = ")
z = input("z = ")
# a)
a = (((abs(x - 1)) ** (0.5)) - ((abs(y)) ** (1/3)))/(1 + (x ** 2)/2 + (y ** 2)/4)
b = x * (atan(z) + exp(-(x + 3)))
print "a) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# b)
a = (3 + exp(y - 1)) / (1 + (x ** 2) * abs(y - tan(z)))
b = 1 + abs(y - x) + (((y - x) ** 2) / 2) + (((y - x) ** 3) / 3)
print "b) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# c)
a = (1 + y) * (((x + y) / (x ** 2 + 4)) / (exp(-x - 2) / (x ** 2 + 4)))
b = (1 + cos(y - 2)) / ((x ** 4) / (2 + (sin(z) ** 2)))
print "c) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# d)
a = y + x / ((y ** 2) + abs((x ** 2) / (y + (x ** 3) / 3)))
b = (1 + (tan(z / 2)) ** 2)
print "d) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# e)
a = (2 * cos(x - pi / 6)) / (1 / 2 + (sin(y) ** 2))
b = 1 + (z ** 2) / (3 + (z ** 2) / 5)
print "e) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# f)
a = ((1 + (sin(x + y) ** 2)) / (2 + abs(x - (2 * x) / (1 + (x ** 2) * (y ** 2))))) + x
b = (cos(atan(1 / z))) ** 2
print "f) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))
# g)
a = log(abs((y - sqrt(abs(x))) * (x - y / (z + (x ** 2) / 4))))
b = x - ((x ** 2) / factorial(3)) + ((x ** 5) / factorial(5))
print "d) a = {:<10}".format(str(a)) + "\tb = {:<10}".format(str(b))