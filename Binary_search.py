def binary_search(array,item, begin=0, end= None, loops=0):
    if end is None:
        end= len(lista) -1

    if begin <= end:
        m = (begin + end)//2
        loops+=1
        if array[m] == item:
            return f"numero encontrado no indice {m} e loops para encontrar = {loops}"
        if array[m] < item:
            return binary_search(array,item, m + 1 , end, loops)
        else:
            return binary_search(array,item, begin,m -1 , loops)
    

lista = [1,2,3,4,5,6,7,8,9]

print(binary_search(lista, 5))