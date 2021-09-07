from decimal import *
import math
#alterando a precisão de cálculo para 14
getcontext().prec = 14

print("\nFunção 1 -> exp(-x²)-cos(x)\n")

def f1(x):
    return math.e**(-x**2)-math.cos(x)

def g1(x):
    return x -1*f1(x)

x0 = 1.5
tol = 1*10**(-7)
iter = 0

while(abs(f1(x0)) > tol):
    x0 = g1(x0)
    print("x = {:.14f} | f(x) = {:.14f}".format(x0,f1(x0)))
    iter += 1
print("Iterações = {}".format(iter))

print("\nFunção 2 -> x³-x-1\n")

def f2(x):
    return x**3-x-1

def g2(x):
    return (x+1)**(1/3)

x = 0.5
tol = 1*10**(-5)
iter = 0

while(abs(f2(x)) > tol):
    x = g2(x)
    iter += 1
    print("x = {:.14f} | f(x) = {:.14f} ".format(x,f2(x)))
print("Iterações = {}".format(iter))

print("\nFunção 3 -> x³-9x+2\n")

def f3(x):
    return x**3-9*x+2

def g3(x):
    return (x**3+2)/9

x = 0
tol = 1*10**(-10)
iter = 0

while(abs(f3(x)) > tol):
    x = g3(x)
    iter += 1
    print("x = {:.14f} | f(x) = {:.14f} ".format(x,f3(x)))
print("Iterações = {}".format(iter))

