n = int(input())
res = True
i = 0
while res:
    if (1 << i) >= n:
        print(i)
        break
    i += 1