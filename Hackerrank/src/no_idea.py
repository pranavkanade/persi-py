from itertools import groupby
if __name__ == "__main__":
    n, m = map(int, input().split(' '))
#     print(type(n), n)
    arr = list(map(int, input().split(' ')))
    a = set(map(int, input().split(' ')))
    b = set(map(int, input().split(' ')))
#     print(arr)
    arr = [(sum(1 for _ in i), int(e)) for e, i in groupby(arr)]
    tot = 0
    for (c, d) in arr:
        if d in a:
            tot += c
        elif d in b:
            tot -= c
    print(tot)