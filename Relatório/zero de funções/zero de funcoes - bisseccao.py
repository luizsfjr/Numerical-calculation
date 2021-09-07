from decimal import *
import math
#alterando a precisão de cálculo para 14
getcontext().prec = 14
def teste1(a,b):
    fa = math.exp(-(a**2)) - math.cos(a)
    fb = math.exp(-(b**2)) - math.cos(b)
    if(fa * fb < 0):
        return True
    else:
        return False
print("-----------------------------")
print("Função 1 -> exp(-x²)-cos(x)")
print("-----------------------------")

#intervalo e tolerância
a = 1.0
b = 1.5
tol = 1*10**(-7)

if(teste1(a,b)):
    it = 0
    solucao = (a+b)/2
    erro = solucao
    while(erro > tol):
        if(not teste1(a,solucao)):
            a = solucao
        else:
            b = solucao
        x0 = solucao
        solucao = (a+b)/2
        erro = abs(solucao-x0)
        print("a = {:14f} | b = {:.14f} | solucao = {:.14f}".format(a,b,solucao))
        it += 1
    print("\nf1(x) = {:.14f} | Iterações = {} \n".format(math.exp(-(solucao**2))-math.cos(solucao), it))    
else:
    print("fail")
print("-----------------------------")
print("Função 2 -> x³-x-1")
print("-----------------------------")

#INTERVALO
a = 0
b = 1.5
tol = 1*10**(-5)

def teste2(a,b):
    fa = a**3-a-1
    fb = b**3-b-1
    if(fa * fb < 0):
        return True
    else:
        return False

if(teste2(a,b)):
    it = 0
    solucao = (a+b)/2
    erro = solucao
    while(erro > tol):
        if(not teste2(a,solucao)):
            a = solucao
        else:
            b = solucao
        x0 = solucao
        solucao = (a+b)/2
        erro = abs(solucao-x0)
        print("a = {:14f} | b = {:.14f} | solucao = {:.14f} ".format(a,b,solucao))
        it += 1
    print("\nf2(x) = {:.14f} | Iterações = {} \n".format(solucao**3-solucao-1, it))    
else:
    print("fail")
print("------------------------------")
print("Função 3 -> x³-9x+2")
print("------------------------------")
def teste3(a,b):
    fa = a**3-9*a+2
    fb = b**3-9*b+2
    if(fa * fb < 0):
        return True
    else:
        return False

#intervalo
a = 0
b = 1
tol = 1*10**(-10)

if(teste3(a,b)):
    it = 0
    solucao = (a+b)/2
    erro = solucao
    while(erro > tol):
        if(not teste3(a,solucao)):
            a = solucao
        else:
            b = solucao
        x0 = solucao
        solucao = (a+b)/2
        erro = abs(solucao-x0)
        print("a = {:14f} | b = {:.14f} | solucao = {:.14f}".format(a,b,solucao))
        it += 1
    print("\nf3(x) = {:.14f} | Iterações = {} \n".format(solucao**3-9*solucao+2,it))
else:
    print("fail")