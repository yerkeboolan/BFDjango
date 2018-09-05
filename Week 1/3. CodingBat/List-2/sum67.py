def sum67(nums):
  move = True
  sum = 0
  
  for n in nums:
    if n == 6:
      move = False
    if move:
      sum += n
      continue
    if n == 7:
      move = True
  return sum
