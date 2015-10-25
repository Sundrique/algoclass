def MergeAndCountSplit(left, right):
    result = []
    inverses = 0
    n = len(left) + len(right)
    i = 0
    j = 0
    for k in range(0, n):
        if i < len(left) and (j >= len(right) or left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            inverses += (len(left) - i)
            result.append(right[j])
            j += 1

    return result, inverses


def SortAndCount(a):
    if len(a) < 2:
        return a, 0
    left, x = SortAndCount(a[0:len(a) / 2])
    right, y = SortAndCount(a[len(a) / 2:])
    merged, z = MergeAndCountSplit(left, right)
    return merged, x + y + z


fileName = 'IntegerArray.txt'
numbers = [int(line.rstrip('\r\n')) for line in open(fileName)]

sorted, inversions = SortAndCount(numbers)
print inversions