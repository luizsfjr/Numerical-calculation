from decimal import *
#alterando a precisão de cálculo para 14
getcontext().prec = 14


grau = int(input("Digite o grau da função: "))
#armazena o(s) valore(s) da função
valores = {}
#armazena a(s) solução(ões)
solucoes = {}

#verifica se a função tem ao menos uma solução
def teste(a,b):
    res1 = valores["ind"]
    res2 = valores["ind"]
    for i in range(0,grau):
        res1 += valores["x"+str(i)]*a**(grau-i)
        res2 += valores["x"+str(i)]*b**(grau-i)
    if(res1 * res2 < 0):
        return True
    else:
        return False

#Leitura de dados
for i in range(0,grau):

    valores["x"+str(i)] = float(input("Digite o coeficiente da incógnita de grau {}: ".format(grau-i)))
    solucoes["x"+str(i)] = valores["x"+str(i)]

    if(grau-1 == i):

        valores["ind"] = float(input("Digite o valor do termo independente: "))

a,b = map(float,input("Digite o intervalo: ").split())
erro = float(input("Digite o erro: "))

#Cálculos
if(teste(a,b)):
    it = 0
    while(abs(b-a) > erro):
        it += 1
        for k in range(0,grau):
            solucoes.update({"x"+str(k):(a+b)/2})
        if(not teste(a,solucoes["x"+str(k)])):
            a = solucoes["x"+str(k)]
        else:
            b = solucoes["x"+str(k)]
    print("\nQuantidade de iterações: {}\n".format(it))
    print("\nSoluções:\n")
    for i in range(0,grau):
        print("x{} = {:.14f}".format(i,solucoes["x"+str(i)]))
    print("\n")
else:
    print("S/ solução real")