def date_fashion(you, date):
  if date <= 2 or you <= 2:
    return 0
  elif date >= 8 or you >= 8:
    return 2
  else:
    return 1
