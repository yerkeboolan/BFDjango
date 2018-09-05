def lone_sum(a, b, c):
  total = 0
  
  if a != b and a != c:
    total += a
  if b != a and b != c:
    total += b
  if c != a and c != b:
    total += c
  
  return total
