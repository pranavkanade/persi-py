from itertools import groupby
S = input()
print(" ".join(["(%d, %d)" % (sum(1 for _ in i), int(e)) for e, i in groupby(S)]))