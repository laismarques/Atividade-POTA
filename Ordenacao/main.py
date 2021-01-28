from Insertion_Sort import InsertionSort
from Bubble import bubbleSortOtimizacao 
import random
import matplotlib.pyplot as plt


randomlist = []
for i in range(0,100):
    n = random.randint(0,100)
    randomlist.append(n)
print(randomlist)

inicio = time.time()
InsertionSort(randomlist)
fim = time.time()
insertion = (fim - inicio)

inicio = time.time()
bubbleSortOtimizacao(randomlist)
fim = time.time()
bubble = (fim - inicio)

plt.hist(x)
plt.show()

