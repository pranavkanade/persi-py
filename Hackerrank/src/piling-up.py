if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        inp_arr = list(map(int, input().split()))

        r = False
        f = False
        z = -1
        for i in range(1, n):
            if inp_arr[i-1] > inp_arr[i] and r is True:
                f = True
                break
            if inp_arr[i-1] > inp_arr[i]:
                r = False
            elif inp_arr[i-1] < inp_arr[i]:
                r = True
        if f is True:
            print("No")
        else:
            print("Yes")