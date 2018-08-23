if __name__ == "__main__":
    S = input()
    d = dict()
    for c in S:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    li = [(d[x], x) for x in d.keys()]
    li.sort(key=lambda x: (x[1]),reverse=False)
    li.sort(key=lambda x: x[0], reverse=True)
    for x, y in li[:3]:
        print("%s %d" % (y,x))
