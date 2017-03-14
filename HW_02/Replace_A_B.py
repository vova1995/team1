'''
Created on Mar 14, 2017

@author: vodachuk
'''
A = 23
B = 15
print "A = ", A , "B = ", B
A, B = B, A
#after replace
print "A = ", A , "B = ", B

#Another version

A = A + B
B = A - B
A = A - B
print "A = ", A , "B = ", B