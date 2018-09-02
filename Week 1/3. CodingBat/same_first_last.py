def same_first_last(nums):
  if len(nums) > 0 and nums[0] - nums[len(nums) - 1] == 0:
    return True
  return False
