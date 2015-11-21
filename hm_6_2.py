import heapq

fileName = 'Median.txt'
numbers = [int(line.rstrip('\r\n')) for line in open(fileName)]

medians = []
lowHeap = []
highHeap = []

for n in numbers:
    if len(lowHeap) == 0 or n <= lowHeap[0][1]:
        heapq.heappush(lowHeap, (-n, n))
    else:
        heapq.heappush(highHeap, (n, n))

    if len(lowHeap) - len(highHeap) > 1:
        min = heapq.heappop(lowHeap)[1]
        heapq.heappush(highHeap, (min, min))
    elif len(lowHeap) < len(highHeap):
        max = heapq.heappop(highHeap)[1]
        heapq.heappush(lowHeap, (-max, max))

    medians.append(lowHeap[0][1])


print divmod(sum(medians), 10000)[1]