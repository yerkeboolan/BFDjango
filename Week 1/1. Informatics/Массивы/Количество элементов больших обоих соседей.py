n = int(input())
s = input().split(' ')
arr = [int(i) for i in s]
res = 0
for index in range(1,len(arr)-1):
    if (arr[index] > arr[index-1] and arr[index] > arr[index+1]):
        res += 1
print(res)
