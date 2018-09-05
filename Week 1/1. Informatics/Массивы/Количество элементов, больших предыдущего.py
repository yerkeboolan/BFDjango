n = int(input())
s = input().split(' ')
arr = [int(i) for i in s]
res = 0
cnt = arr[0]
for index, i in enumerate(arr[:len(arr)]):
    if (arr[index-1] > 0 and arr[index] > 0) or (arr[index-1] < 0 and arr[index] < 0):
        print("YES")
        break
else:
    print("NO")