def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  if a.endswith(b) or b.endswith(a):
    return True
  return False
  
