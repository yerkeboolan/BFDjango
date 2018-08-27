def front_back(str):
  mid = str[1:len(str)-1]
  if(len(str) < 2):
    return str
  else:
    return(str[len(str)-1] + mid + str[0])
