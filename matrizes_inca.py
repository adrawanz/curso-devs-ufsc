def sou_piramide_inca(a):
    piramide = True
    tamanho = len(a)
    inicio = 0
    fim = tamanho - 1
    while tamanho >= 2:
        for i in range(inicio, fim):
            if a[inicio][i]+1 != a[inicio][i+1]:
                piramide = False
                break
        if piramide:
            for i in range(inicio, fim):
                if a[i][fim] + 1 != a[i + 1][fim]:
                    piramide = False
                    break
        if piramide:
            for i in range(inicio, fim):
                if a[fim][i] - 1 != a[fim][i+1]:
                    piramide = False
                    break
        if piramide:
            for i in range(inicio+1, fim):
                if a[i][inicio] - 1 != a[i+1][inicio]:
                    piramide = False
                    break
        if piramide:
            if tamanho > 24:
                if a[inicio+1][inicio] + 1 != a[inicio+1][inicio+1]:
                    piramide = False
                    break

        tamanho -= 2
        inicio += 1
        tamanho -= 1
    return piramide

# Principal
##matriz =[[1,  2,  3,  4],
##        [12, 13, 14, 5],
##        [11, 16, 15, 6],
##        [10,  9,  8, 7]]
##
##matriz =[[1,  2,  3,  4],
##        [12, 13, 14, 5],
##        [11, 16, 15, 6],
##        [10,  9, 18, 7]]
##
##matriz = [[12, 13, 14],
##         [19, 20, 15],
##         [18, 17, 16]]

######## Inicio leitura da matriz ############
tam = int(input())  # Entrar com o número de linhas/colunas da matriz
matriz = []
for i in range(tam):  # Laço para mudar linhas
    a = []
    for j in range(tam):  # Laço para mudar colunas
        a.append(int(input()))  # Lê elementos da matriz
    matriz.append(a)
######## fim leitura da matriz ############

# Chamada da função
if sou_piramide_inca(matriz):
    print(True)
else:
    print(False)
