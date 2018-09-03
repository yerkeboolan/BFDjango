def array_front9(nums):
  rng = len(nums)
  if rng > 4:
    rng = 4
  for i in range(rng):
    if nums[i] == 9:
      return True
  return False
    
