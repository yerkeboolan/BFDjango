def xyz_there(str):
  for i in range(len(str) - 2):
    if i > 0:
      if str[i:i+3] == "xyz" and str[i-1] != ".":
        return True
    elif str[i:i+3] == "xyz":
      return True
  return False
