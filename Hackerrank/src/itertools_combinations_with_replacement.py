import itertools

if __name__ == '__main__':
    string, k = input().split(' ')
    k = int(k)
    out = list(itertools.combinations_with_replacement(sorted(string), k))
    # print(len(out))
    out = [''.join(o) for o in out]
    for o in out:
        print(o)
