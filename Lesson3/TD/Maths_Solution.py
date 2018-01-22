# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:47:00 2018

@author: ndoannguyen
"""

import numpy as np
import scipy as sp
from scipy import optimize

A = np.array([ [ 0, 1,  0,  0], 
               [ 1, 2, -2,  0],
               [ 1, 0,  1, -1],
               [-1, 2, -1,  1]])
               
B = np.array([ [-1,  2,  2, -1], 
               [ 0,  1, -1,  0],
               [ 2, -2, -1,  1],
               [ 0,  0,  1,  1]])
               
MatA = np.matrix([ [ 0, 1,  0,  0], 
                   [ 1, 2, -2,  0],
                   [ 1, 0,  1, -1],
                   [-1, 2, -1,  1]])
                  
MatB = np.matrix([ [-1,  2,  2, -1], 
                   [ 0,  1, -1,  0],
                   [ 2, -2, -1,  1],
                   [ 0,  0,  1,  1]])

v = np.array([2, 3, 1, 3])
Matv = np.matrix(v).transpose()

I = np.identity(4)

MatI = np.matrix(I)
                
# Exercise 1
def ex1():
    print( A.dot(B).dot(A).dot(B).dot(A).dot(B).dot(A).dot(B).dot(A).dot(B) )
    print( (MatA*MatB)**5 )
    print( (MatA.dot(MatB))**5 )

# Exercise 2
def ex2():
    print( A.dot(v) )
    print( A.dot(v.transpose() ))
    print( MatA*Matv )

    print( B.transpose().dot(v) )
    print( MatB.transpose()*Matv )

    print( v.dot(A).dot(v) )
    print( Matv.transpose() * MatA * Matv)

# Exercise 3
def ex3():
    print ( np.linalg.inv(A + I) )
    print ( np.linalg.inv(MatA + MatI) )

# Exercise 4
def ex4():
    C = A[:3]
    U, eigenvectors, Vtranspose = np.linalg.svd(C)
    Sigma = np.zeros((3, 4))
    np.fill_diagonal(Sigma, eigenvectors)
    V = Vtranspose.transpose()
    print U, "\n", Sigma, "\n", V
    print "Verification: U * Sigma * V^t = ", np.matrix(U) * np.matrix(Sigma) * np.matrix(V).transpose()

# Exercise 5
def ex5():
    eigvals, eigvecs = np.linalg.eig(A)
    print eigvals
    print eigvecs
    print "Verification: ", eigvecs.dot(np.diag(eigvals)).dot(np.linalg.inv(eigvecs))
    print( np.ndim(A) )

# Exercise 6
def ex6():
    eigvals = np.linalg.eigvals(A)
    charpoly = np.poly(eigvals)
    print(charpoly)
    print( np.linalg.det(A) )
    print( np.trace(A) )

# Exercise 7
def ex7():
    print( np.eye(4) )
    print( np.linalg.solve((A + np.eye(4)), v) )

f = lambda x: 4 * np.sin(x) - np.cos(x) + 2 * np.exp(-3*x**2) + 1./x 
F = lambda x: float((x[0] - x[1])**2) / (x[0]**2 + x[1]**2)
#F = lambda x: x[0] + x[1]**2

# Exercise 8
def ex8():
    print( sp.misc.derivative(f, 3.0, dx = 1e-6, n = 1) )
    print( sp.misc.derivative(f, 3.0, dx = 1e-6, n = 2) )
    print( sp.misc.derivative(f, 3.0, dx = 1e-6, n = 3, order = 7) )
    print( sp.misc.derivative(f, 3.0, dx = 1e-6, n = 4, order = 7) )

#Exercise 9
def ex9():
    print( optimize.approx_fprime((1, -2), F, 1e-8))


    
if __name__ == "__main__":
    ex9()