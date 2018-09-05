n = int(input())
s = input().split(' ')
arr = [int(i) for i in s]
res = 0
for i in arr:
    if i > 0:
        res += 1
print(res)
