from decimal import *
import math
#alterando a precisão de cálculo para 14
getcontext().prec = 14

print("\nFunção 1 -> exp(-x²)-cos(x)\n")

def f1(x):
    return math.exp(-(x**2))-math.cos(x)

def df1(x):
    return -2*math.exp(-(x**2))*x+math.sin(x)

#Função 1
iter = 0
tol = 1*10**(-7)
x = 1.5 #chute inicial

while(abs(f1(x)) > tol):
    iter += 1
    dx = -(f1(x)/df1(x))
    x = x + dx
    print("f(x) = {:.14f}  |  x = {:.14f}".format(f1(x),x))
print("Quantidade de iterações = {}".format(iter))
print("\nFunção 2 -> x³-x-1\n")

def f2(x):
    return x**3-x-1

def df2(x):
    return 3*(x**2)-1

tol = 1*10**(-5)
x = 0
iter = 0

while(abs(f2(x)) > tol):
    iter += 1
    dx = -(f2(x)/df2(x))
    x = x + dx
    print("f(x) = {:.14f}  |  x = {:.14f}".format(f2(x),x))
print("Quantidade de iterações = {}".format(iter))

print("\nFunção 3 -> x³-9x+2\n")

def f3(x):
    return x**3-9*x+2
def df3(x):
    return 3*(x**2)-9

tol = 1*10**(-10)
x = 0
iter = 0

while(abs(f3(x)) > tol):
    iter += 1
    dx = -(f3(x)/df3(x))
    x = x + dx
    print("f(x) = {:.14f}  |  x = {:.14f}".format(f3(x),x))
print("Quantidade de iterações = {}".format(iter))
