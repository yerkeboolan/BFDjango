import math
a = int(input())
b = int(input())
arr = [str(i) for i in range(a, b+1) if i == int(math.sqrt(i)) ** 2]
print(' '.join(arr))