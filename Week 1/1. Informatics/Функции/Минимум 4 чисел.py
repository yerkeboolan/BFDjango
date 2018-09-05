def min4(a, b, c, d):
    return min(min(a,b),min(c,d))

s = input().split(" ")
arr = [int(i) for i in s]
print(min4(arr[0], arr[1], arr[2], arr[3])
	