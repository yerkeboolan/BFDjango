a = int(input())
b = int(input())
c = int(input())
d = int(input())
arr = [str(i) for i in range(a, b+1) if i % d == c]
print(' '.join(arr))