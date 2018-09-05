def power(a, b):
    return  a ** b

s = input().split(" ")
arr = [float(i) for i in s]
print(power(arr[0], arr[1]))