def countSort(vetor, digito):
    #maior = encontrarMaior(vetor)
    count = [[] for i in range(10)]
    #Definindo o Dicionário.

    for i in range(len(vetor)):
        indice = (vetor[i]/digito)
        count[int((indice)%10)].append(vetor[i])
    
    indice = 0
    for i in range(10):
        if len(count[i]) > 0:
            for j in range(len(count[i])):
                vetor[indice] = count[i][j]
                indice += 1

def contaDigitos(num):
    conta = 0
    while num > 0:
        conta += 1
        num = num // 10

    print(conta)
    return conta
    
def radixSort(vetor):
    decimais = contaDigitos(max(vetor))
    index = 1
    for i in range(decimais):
        countSort(vetor, index)
        index *= 10



vetor = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(vetor)
print(vetor)
