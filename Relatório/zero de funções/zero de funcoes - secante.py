from decimal import *
import math
#alterando a precisão de cálculo para 14
getcontext().prec = 14

print("\nFunção 1 -> exp(-x²)-cos(x)\n")

def f1(x):
    return math.exp(-(x**2))-math.cos(x)

x0 = 1
x1 = 1.5
tol = 1*10**(-7)
it = 0

while(abs(f1(x1)) > tol):
    aux = x1
    x1 = (x0*f1(x1)-x1*f1(x0))/(f1(x1)-f1(x0))
    x0 = aux
    it += 1
    print("F(x) = {:.14f} | x = {:.14f}".format(f1(x1),x1))
print("Quantidade de iterações = {}".format(it))

print("\nFunção 2 -> x³-x-1\n")

def f2(x):
    return x**3-x-1

x0 = 0
x1 = 0.5
tol = 1*10**(-5)
it = 0

while(abs(f2(x1)) > tol):
    aux = x1
    x1 = (x0*f2(x1)-x1*f2(x0))/(f2(x1)-f2(x0))
    x0 = aux
    it += 1
    print("F(x) = {:.14f} | x = {:.14f}".format(f2(x1),x1))
print("Quantidade de iterações = {}".format(it))

print("\nFunção 3 -> x³-9x+2\n")

def f3(x):
    return x**3-9*x+2

x0 = -0.5
x1 = 0
tol = 1*10**(-10)
it = 0

while(abs(f3(x1)) > tol):
    aux = x1
    x1 = (x0*f3(x1)-x1*f3(x0))/(f3(x1)-f3(x0))
    x0 = aux
    it += 1
    print("F(x) = {:.14f} | x = {:.14f}".format(f3(x1),x1))
print("Quantidade de iterações = {}".format(it))