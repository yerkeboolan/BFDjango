def count_evens(nums):
  s = 0
  for num in nums:
    if num % 2 == 0:
      s += 1
  return s
