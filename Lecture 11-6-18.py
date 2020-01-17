#11/6/18 lecture



#Selection sort

def selectionSort(aList):
    
    for i in range(len(aList)):
        smallest = i
        #search smallest element in remaining list
        for j in range(i, len(aList)):
            if aList[j] < aList[smallest]:
                smallest = j
        #swap smallest & first element  
        if smallest != i:
            temp = aList[i]
            aList[i] = aList[smallest]
            aList[smallest] = temp

    return aList


a = [10, 8, 12, 6, 17, 100, 2]
b = selectionSort(a)
print(b)

c = ['z', 'b', 'l', 'k', 'c', 'o']
print(selectionSort(c))


#Insertion sort

def insertionSort(someList):

    for i in range(1, len(someList)):
        currentValue = someList[i]
        j = i

        while j > 0 and someList[j-1] > currentValue:
            someList[j] = someList[j-1]
            j = j - 1

        someList[j] = currentValue
    return someList

a = [10, 8, 12, 6, 17, 100, 2]
b = insertionSort(a)
print(b)

c = ['z', 'b', 'l', 'k', 'c', 'o']
print(insertionSort(c))


#Quick sort

def quickSort(l):
    



a = [10, 8, 12, 6, 17, 100, 2]
b = quickSort(a)
print(b)

c = ['z', 'b', 'l', 'k', 'c', 'o']
print(quickSort(c))
