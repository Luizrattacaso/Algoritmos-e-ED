#O Selection Sort faz uma varedura dos elementos
# e identifica o menor entre eles e vai trocando as posições entre os elementos

lista = [7,5,1,8,3]

def selection_sort(lista):

    min_index=0
    for i in range(len(lista) -1):
        min_index = i

        for j in range(i,len(lista)-1):
            if lista[j] < lista[min_index]:
                min_index = j

        if lista[i] > lista[min_index]:
            aux = lista[i]
            lista[i] = lista[min_index]
            lista[min_index] = aux

    return lista

print(selection_sort(lista))