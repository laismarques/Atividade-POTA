def MergeSort(vetor, inicio , fim):
    if inicio < fim:
        meio = int((inicio + fim)// 2)
        MergeSort(vetor, inicio, meio)
        MergeSort(vetor, meio+1, fim)
        Intercala(vetor, inicio, meio, fim, aux)
    

def Intercala(vetor, inicio, meio, fim, aux):
    for i in range(inicio):
        aux[i] = vetor[i]
        print("teste")
    for j in range(meio+1, fim):
        aux[fim + meio + 1 - j] = vetor[j]
    i = inicio
    j = fim
    print(aux)
    for k in range(inicio, fim):
        if aux[i] <= aux[j]:
            print(aux[i])
            vetor[k] = aux[i]
            i = i + 1
        else:
            vetor[k] = aux[j]
            j = j - 1

vetor = [9, 8, 6, 12, 4, 3, 7]
aux = vetor
print(aux)
MergeSort(vetor, 0, 6)
print(vetor)