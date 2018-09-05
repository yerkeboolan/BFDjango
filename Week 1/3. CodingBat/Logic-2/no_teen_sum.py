def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
def fix_teen(n):
  if n in range(13, 15) or n in range(17, 20):
    return 0
  return n