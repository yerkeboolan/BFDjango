def front3(str):
  three = 3
  if(len(str) < three):
    three = len(str)
  start = str[:three]
  return start + start + start
