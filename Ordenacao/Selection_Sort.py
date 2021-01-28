def SelectionSort(vetor):
    for i in range(len(vetor)):
        minimo = i
        for j in range(i +1,len(vetor)):
            if vetor[j] < vetor[minimo]:
                minimo = j
        vetor[i], vetor[minimo] = vetor[minimo], vetor[i]
    print(vetor)

vetor = [9,8,6,12,4,3]
SelectionSort(vetor)