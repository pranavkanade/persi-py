import itertools

if __name__ == "__main__":
    n = int(input())
    inl = input().split(' ')
    m = int(input())

    comb = list(itertools.combinations(range(n), m))
    # print(comb)
    res = 0
    for club in comb:
        for i in range(m):
            if inl[club[i]].lower() == 'a':
                res += 1
                break
    print(res/len(comb))