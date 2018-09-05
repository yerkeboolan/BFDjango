if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    t = arr[::-1]
    for i in range(len(t)):
        if t[i] != t[i+1]:
            print t[i+1]
            break