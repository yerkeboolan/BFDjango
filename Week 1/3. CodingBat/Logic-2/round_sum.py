def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(x):
  if x % 10 == 0:
    return x
  elif x % 10 >= 5:
    return (x/10 + 1) * 10
  elif x % 10 < 5:
    return (x/10) * 10
    
