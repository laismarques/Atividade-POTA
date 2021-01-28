import random
import time

def InsertionSort(vetor):     
    for i in range(len(vetor)-1, -1, -1):         
        j = i           
        while (j > 0):  
            if (vetor[j-1] > vetor[i]):   
                vetor [j-1], vetor[i] = vetor[i], vetor[j-1]             
            print(vetor)             
            j = j - 1   
vetor = [16,15,23,5,1,2,3]  
InsertionSort(vetor) 
print(vetor)

