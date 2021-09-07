ordem = int(input("Digite a ordem do sistema: "))

print("\n")
sistema = input("Digite I para sist. triangular inferior ou S para sist. triangular superior: ")

def cria_dic(ordem):
    lista = []
    for i in range(0,ordem):
        lista.append(dict())
    return lista
equacoes = cria_dic(ordem)

resultados = {}
for i in range(0,ordem):
    resultados.update({"x"+str(i+1): 0})

for j in range(1,ordem+1):
    print("\n")
    print("Equação {}:".format(j))
    print("\n")
    for i in range(1,ordem+1):
        sinal = ""
        coef = float(input("Digite o coeficiente de x{}: " .format(i)))
        equacoes[j-1].update({"x"+str(i): coef})
    equacoes[j-1].update({"res"+str(j): float(input("Digite o resultado da equação {}:".format(j)))})

if(sistema.upper() == "S"):
    i = ordem-1
    j = ordem
    acumulador = 0
    resultados.update({"x"+str(ordem):equacoes[i]["res"+str(ordem)]/(equacoes[i]["x"+str(ordem)])})
    while(i > 0):
        acumulador = 0 
        j = ordem
        while(j > 0):
            if(j != i):
                acumulador += resultados["x"+str(j)]*equacoes[i-1]["x"+str(j)]
            j  -= 1
        resultados.update({"x"+str(i): (equacoes[i-1]["res"+str(i)]-acumulador)/equacoes[i-1]["x"+str(i)]})    
        i -= 1
elif(sistema.upper() == "I"):
    print("aaaaa")
    i = 1
    j = 0
    acumulador = 0
    resultados.update({"x1":equacoes[0]["res1"]/(equacoes[0]["x1"])})
    while(i < ordem):
        acumulador = 0 
        j = 0
        while(j < ordem):
            if(j != i):
                acumulador += resultados["x"+str(j+1)]*equacoes[i]["x"+str(j+1)]
            j  += 1
        resultados.update({"x"+str(i+1): (equacoes[i]["res"+str(i+1)]-acumulador)/equacoes[i]["x"+str(i+1)]})    
        i += 1

#print(equacoes)
for i in resultados:
    print("{} = {:.2f}".format(i,resultados[i]))
