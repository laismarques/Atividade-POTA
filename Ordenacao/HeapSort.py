from math import floor

def troca(a, 
          i, 
          j):
    
    a[i], a[j] = a[j], a[i]

def arruma_heap(a, 
                inicio, 
                fim):

    raiz = inicio

    while raiz * 2 + 1 <= fim:
        filho = raiz * 2 + 1
        trocar = raiz
        if a[trocar] < a[filho]:
            trocar = filho
        if filho + 1 <= fim and a[trocar] < a[filho + 1]:
            trocar = filho + 1
        if trocar == raiz:
            break
        else:
            troca(a, raiz, trocar)
            raiz = trocar

def cria_heap(a,
              tamanho):

    inicio = floor((tamanho - 2)/2)
 
    while inicio >= 0:
        arruma_heap(a, inicio, tamanho -1)
        inicio -= 1

def heap_sort(a, 
              tamanho):
    
    cria_heap(a, tamanho)

    fim = tamanho - 1
    while fim > 0:
        troca(a, 0, fim)
        fim = fim - 1
        arruma_heap(a, 0, fim)

lista = [5, 8, 2, 45, 6, 5, 3]
heap_sort(lista, 7)
print(lista)