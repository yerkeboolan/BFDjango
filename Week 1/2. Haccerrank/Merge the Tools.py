def merge_the_tools(string, k):
    arr = []
    for i in range(0, len(string), k):
        arr.append(string[i:i+k])
    res = []
    for sub in arr:
        unique_list = []
        for c in sub:
            if c not in unique_list:
                unique_list.append(c)
        res.append(''.join(unique_list))
    for i in res:
        print(i)