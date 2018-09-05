n = int(input())
res = True
i = 0
while res:
    if (1 << i) == n:
        print("YES")
        break
    elif (1 << i) > n:
        res = False
    i += 1
else:
    print("NO")