def quick_sort(array):

    if len(array)<2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)
    
lista = [12,43,78,26,24,55,17,25,33]

print(quick_sort(lista))