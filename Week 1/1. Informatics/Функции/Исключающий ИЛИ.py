def xor(a, b):
    return  int(a ^ b)

s = input().split(" ")
arr = [int(i) for i in s]
print(xor(arr[0], arr[1]))