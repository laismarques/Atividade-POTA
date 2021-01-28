import random

def verifica_quantidade(vetor) -> None:
    '''
    Função cria um dicinário com os valores possíveis
    na com valores default 0 e incrementa o valor conforme ele 
    aparece no vetor

    Retorno:
    Nenhum

    '''
    dic = {}
    for i in range(50, 101):
        dic.setdefault(i, 0)

    for i in range(len(vetor)):
        dic[vetor[i]] +=1

    for i in range(50, 101):
        print("O valor ", i, " apareceu ", dic[i], " vezes")

n = 10 ## é possível alterar o tamanho do vetor
vetor = [random.randint(50, 100) for _ in range(n)]
print(vetor)
verifica_quantidade(vetor)

