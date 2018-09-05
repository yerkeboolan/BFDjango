
from itertools import groupby
print(*[(len(list(occurance)), int(char)) for char, occurance in groupby(input())])