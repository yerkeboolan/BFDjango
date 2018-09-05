n = int(input())
s = input().split(' ')
arr = [int(i) for i in s]
res = arr[::2]
for i in res:
    print(i, end = ' ')