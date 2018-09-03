def front_times(str, n):
  res = ""
  length = 3
  if length > len(str):
    length = len(str)
  ln = str[:length]
  
  for i in range(n):
    res += ln 
  return res
  
