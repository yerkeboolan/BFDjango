a = int(input())
for i in range(2, 30001):
    if a % i == 0:
        print(i)
        break