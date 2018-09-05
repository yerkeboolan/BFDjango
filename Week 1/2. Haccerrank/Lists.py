if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        command, *s = input().split()
        nums = list(map(int, s))
        if command == "insert":
            arr.insert(nums[0], nums[1])
        elif command == "print":
            print(arr)
        elif command == "remove":
            arr.remove(nums[0])
        elif command == "append":
            arr.append(nums[0])
        elif command == "sort":
            arr.sort()
        elif command == "pop":
            arr.pop()
        else:
            arr.reverse();