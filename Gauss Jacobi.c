"""Método iterativo de Gauss Jacobi para resolução de Sistemas lineares
   Desenvolvedor: Luiz Carlos da S.F. Junior 
"""
ordem = int(input("Digite a ordem do sistema: "))
solucao = [] #solução do sistema(irá armazenar o resultado da iteração k)
solucao_aux = [] #solução anterior do sistema(irá armazenar o resultado da iteração k-1)

"""inicialização da lista de soluções"""
for i in range(0,ordem):
    solucao.append(0)
    solucao_aux.append(0)

it_inicial = [] #iteração 0 a ser inserida pelo usuário
#entrada de dados
def cria_dic(ordem):
    lista = []
    for i in range(0,ordem):
        lista.append(dict())
    return lista
equacoes = cria_dic(ordem)
v_independente = [] 
for j in range(0,ordem):
    print("\n")
    print("Equacao {}:".format(j+1))
    print("\n")
    for i in range(0,ordem):
        coef = float(input("Digite o coeficiente de x{}: " .format(i)))
        equacoes[j].update({"x"+str(i): coef})
    v_independente.append(float(input("Resultado da equacao {}: ".format(j+1))))

print("\n")
print("Iteracao 0:")
print("\n")
for i in range(0,ordem):
    it_inicial.append(float(input("Digite o valor de x{}:".format(i))))
    solucao_aux[i] = it_inicial[i]

print("\n")
precisao = float(input("Digite a precisao desejada para a solucao: "))
dist_relativa = precisao+1
dist = 0
#inicio da iteração
k = 1
cont = 0
while(dist_relativa > precisao):
    #k = 1 #iterador
    cont = 0
    while(cont < ordem):
        acumulador = 0
        for i in range(0,ordem): #roda linha
            acumulador = 0
            for j in range(0,ordem): #roda coluna
                if(k == 1):
                    if(j != i):
                        acumulador += it_inicial[j]*equacoes[i]["x"+str(j)]
                else:
                    if(j != i):
                        acumulador += solucao_aux[j]*equacoes[i]["x"+str(j)]
            solucao[i] = (v_independente[i]-acumulador)/equacoes[i]["x"+str(i)] #dar pra ir pro final
        cont += 1
    #calculo da distancia e da distancia relativa
    #distancia(dist)
    dist = abs(solucao[0]-solucao_aux[0])
    for i in range(1,ordem):
        if(dist < abs(solucao[i]-solucao_aux[i])):
            dist = abs(solucao[i]-solucao_aux[i])
    dist_relativa = dist/max(solucao)

    #Cópia
    for z in range(0,ordem):
        solucao_aux[z] = solucao[z]
    k += 1

#Exibição da solução
print("\n")
print("Solucao do sistema com precisao de {} encontrada na iteracao {}: ".format(precisao,k-1))
print("\n")
for i in range(0,ordem):
    print("x{} = {:.4f}".format(i,solucao[i]))