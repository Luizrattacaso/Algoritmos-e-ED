def binarySearch(lista,item,comeco,fim,comparacoes):
    comparacoes +=1

    if comeco <=fim:
        middle = (comeco+fim)//2
        if len(lista) == 0:
            return None
        
        if lista[middle] == item:
            return lista[middle], comparacoes
        elif lista[middle] > item:
            return binarySearch(lista,item,comeco,middle - 1,comparacoes)
        elif lista[middle] < item:
            return binarySearch(lista,item,middle + 1,fim,comparacoes)
        else:
            return None

#testes
Lista1 = [11,22,33,44,55,66,77,88,99,101,103,124,156,157,177,180,188,199]
Lista2 =[]

if __name__ == "__main__":
    print(binarySearch(Lista1,199,0,len(Lista1)-1,0))
    print(binarySearch(Lista2,7,0,len(Lista1)-1,0))
    print(binarySearch(Lista1,33,0,len(Lista1)-1,0))
