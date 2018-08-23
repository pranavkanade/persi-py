if __name__ == '__main__':
    n = int(input())
#     n = 4
#     arr = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
    arr = []
    for _ in range(n):
        arr.append(input())
    res = dict()
    resl = []
    for s in arr:
        if s in res.keys():
            res[s] += 1
        else:
            res[s] = 1
            resl.append(s)