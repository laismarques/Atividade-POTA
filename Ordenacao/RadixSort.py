def encontrarMaior(vetor):
    maior = vetor[0]
    for i in range(len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
    
    return maior

def countSort(vetor, digito):
    #maior = encontrarMaior(vetor)
    count = []
    #Definindo o Dicionário.
    aux = {}
    for i in range(10):
        aux.setdefault(i, [])

    for i in range(len(vetor)):
        indice = (vetor[i]/digito)
        aux[int((indice)%10)].append(vetor[i])

    indice = 0
    for i in range(10):
        if len(aux[i]) > 0:
            for j in range(len(aux[i])):
                vetor[indice] = aux[i][j]
                indice += 1 

    
def radixSort(vetor):
    decimais = len(str(max(vetor)))
    index = 1
    for i in range(decimais):
        countSort(vetor, index)
        index *= 10



vetor = [170, 45, 75, 90, 802, 24, 2, 66]
#radixSort(vetor)
teste = [i for i in range(10)]


print(teste)
