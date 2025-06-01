def binarySearch(list,item,begin,end,comparations):
    comparations +=1

    if begin <=end:
        middle = (begin+end)//2

        if list[middle] == item:
            return Lista1[middle], comparations
        elif list[middle] > item:
            return binarySearch(list,item,begin,middle - 1,comparations)
        elif list[middle] < item:
            return binarySearch(list,item,middle + 1,end,comparations)
        else:
            return None

#testes
Lista1 = [11,22,33,44,55,66,77,88,99,101,103,124,156,157,177,180,188,199]
Lista2 =[]
Lista3 = [11,22,33,44,55,66,77,88,99,101,103,124,156,157,177,180,188,199]
if __name__ == "__main__":
    print(binarySearch(Lista1,199,0,len(Lista1)-1,0))
    print(binarySearch(Lista1,7,0,len(Lista1)-1,0))
    print(binarySearch(Lista1,33,0,len(Lista1)-1,0))
