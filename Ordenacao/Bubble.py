def bubbleSort(vetor):
    for i in range(len(vetor) - 1):
        for j in range(len(vetor) - 1):
            if (vetor[j] > vetor[j+1]):
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    
    print(vetor)

def bubbleSortOtimizacao(vetor):
    n = len(vetor)
    
    while (n > 0):
        newn = 0
        for i in range(1, len(vetor)):
            if vetor[i - 1] > vetor[i]:
                vetor[i - 1], vetor[i] = vetor[i], vetor[i - 1]
                newn = i
        n = newn
    print(vetor)
vetor = [6, 8, 9, 4, 2, 1]
bubbleSortOtimizacao(vetor)