import random


def middle(start, end):
    return (start + end) / 2


def ChosePivot(a, start, end):
    return start


def ChosePivotEnd(a, start, end):
    return end


def ChosePivotThreeMedian(a, start, end):
    m = middle(start, end)
    pairs = [(start, a[start]), (m, a[m]), (end, a[end])]
    pairs.sort(key=lambda x: x[1])
    return pairs[1][0]


def ChosePivotRandom(a, start, end):
    return random.randint(start, end)


def Partition(a, start, end):
    partitionIndex = start + 1
    for i in range(start + 1, end + 1):
        if a[i] < a[start]:
            a[i], a[partitionIndex] = a[partitionIndex], a[i]
            partitionIndex += 1

    a[start], a[partitionIndex - 1] = a[partitionIndex - 1], a[start]
    return partitionIndex - 1


def QuickSort(a, start=None, end=None, chosePivot=ChosePivot):
    if start is None:
        start = 0
    if end is None:
        end = len(a) - 1

    if start >= end:
        return 0

    pivotIndex = chosePivot(a, start, end)
    a[pivotIndex], a[start] = a[start], a[pivotIndex]

    partitionIndex = Partition(a, start, end)
    comparisonsLeft = QuickSort(a, start, partitionIndex - 1, chosePivot)
    comparisonsRight = QuickSort(a, partitionIndex + 1, end, chosePivot)

    return end - start + comparisonsLeft + comparisonsRight


fileName = 'QuickSort.txt'
numbers = [int(line.rstrip('\r\n')) for line in open(fileName)]
numbers2 = numbers[:]
numbers3 = numbers[:]

print QuickSort(numbers, chosePivot=ChosePivot)
print QuickSort(numbers2, chosePivot=ChosePivotEnd)
print QuickSort(numbers3, chosePivot=ChosePivotThreeMedian)
print QuickSort(numbers3, chosePivot=ChosePivotRandom)