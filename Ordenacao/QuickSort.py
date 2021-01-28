def particionar(lista,
                inicio,
                fim):

    i = inicio + 1
    j = fim

    while i <= j:
        if lista[i] < lista[inicio]:
            i += 1
        else:
            if lista[j] > lista[inicio]:
                j -= 1
            else:
                lista[i], lista[j] = lista[j], lista[i]
                i += 1
                j -= 1
    lista[inicio], lista[j] = lista[j], lista[inicio] 
    return j

def quick_sort(lista, 
              inicio, 
              fim):

    if inicio < fim:
        meio = particionar(lista, inicio, fim)
        quick_sort(lista, inicio, meio - 1)
        quick_sort(lista, meio + 1, fim)


lista = [4, 7, 34, 7, 9, 1, 3, 2]
quick_sort(lista, 0, 7)
print(lista)
