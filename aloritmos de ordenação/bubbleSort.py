"""analisa elementos que estão em posições subsequentes
mudando de posição de 2 em 2 até que a ordenação esteja completa"""
def bubble_sort(array):
    n = len(array)
    for j in range(n-1):
        for i in range(n-1):
            if array[i] > array[i+1]:
                #troca de posições dos elementos de i e i+1
                array[i],array[i+1] = array[i+1],array[i]
    return array

lista = [12,43,78,26,24,55,17,25,33]

print(bubble_sort(lista))