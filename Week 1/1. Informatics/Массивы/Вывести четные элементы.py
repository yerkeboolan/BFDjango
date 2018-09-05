n = int(input())
m = input().split(' ')
arr = [int(i) for i in m if int(i) % 2 == 0]
for i in arr:
    print(i, end = ' ')