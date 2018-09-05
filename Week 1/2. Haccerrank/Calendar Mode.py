import calendar
arr = list(map(int, input().split()))
print(list(calendar.day_name)[calendar.weekday(arr[2], arr[0], arr[1])].upper())