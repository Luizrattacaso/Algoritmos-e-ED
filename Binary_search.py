def binary_search(array,item, begin=0, end= None, loops=0):
    if end is None:
        end= len(array) -1

    if begin <= end:
        m = (begin + end)//2
        loops+=1
        if array[m] == item:
            return f"numero encontrado no indice {m} e loops para encontrar = {loops}"
        if array[m] < item:
            return binary_search(array,item, m + 1 , end, loops)
        else:
            return binary_search(array,item, begin,m -1 , loops)
    
#testes
lista = [1,2,3,4,5,6,7,8,9]
lista2 = [1,5,9,13,17,21,25,29,33,37,41,45,49,53,57,61,65,69,73,77,81,85,89,93,97]
lista3 = []

print(binary_search(lista3, 5))
