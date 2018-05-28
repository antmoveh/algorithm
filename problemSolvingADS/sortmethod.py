
# 冒泡排序
def bubbleSort(alist):
    for i in range(len(alist)-1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)


def shortBubbleSort(alist):
    exchanges = True
    i = len(alist) - 1
    while i > 0 and exchanges:
        exchanges = False
        for j in range(i):
            if alist[j] > alist[j+1]:
                exchanges = True
                alist[j], alist[j+1] = alist[j+1], alist[j]
        i -= 1


alist2 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist2)
print(alist2)

# 选择排序
def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


alist3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist3)
print(alist3)


# 插入排序
def insertionSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position - 1

        alist[position] = currentvalue


alist4 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist4)
print(alist4)


# 希尔排序
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount//2


def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap
        alist[position] = currentvalue


alist5 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist5)
print(alist5)


# 归并排序
def mergeSort(alist):
    print("Splitting", alist)
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
        print("ALIST", alist)
    print("Merging", alist)


alist6 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist6)
print(alist6)


# 快速排序
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]

    return rightmark


alist7 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist7)
print(alist7)