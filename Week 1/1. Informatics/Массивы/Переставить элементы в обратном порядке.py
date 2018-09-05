n = int(input())
s = input().split(' ')
arr = [int(i) for i in s]
for i in arr[::-1]:
    print(i, end = ' ')