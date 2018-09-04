a = int(input())
res = 0
for i in range(1, a+1):
    if a % i == 0:
        res += 1
print(res)