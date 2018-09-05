def lucky_sum(a, b, c):
  sum = 0
  for n in (a, b, c):
    if n != 13:
      sum += n
    else:
      break
  return sum
