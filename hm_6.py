fileName = '2sum.txt'
numbers = {int(line.rstrip('\r\n')): True for line in open(fileName)}

count = 0
min = -10000
max = 10000
for t in range(min, max + 1):
    for x in numbers:
        y = t - x
        if y != x and y in numbers:
            count += 1
            break

print(count)