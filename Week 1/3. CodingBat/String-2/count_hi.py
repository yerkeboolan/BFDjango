def count_hi(str):
  res = 0
  
  for i in range(len(str) - 1):
    if str[i:i+2] == "hi":
      res = res + 1
  return res