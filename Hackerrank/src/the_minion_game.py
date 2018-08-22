def minion_game(string):
    Kevins_total = 0
    Stuarts_total = 0
    length = len(string)
    for i, each_char in enumerate(list(string)):
        if (each_char.upper() in ['A', 'E', 'I', 'O', 'U']):
            Kevins_total += length - i
        else:
            Stuarts_total += length - i
    # Instrumentation
    # print("Kevin : ", Kevins_total)
    # print("Stuart : ", Stuarts_total)

    if Stuarts_total > Kevins_total:
        print("Stuart %d" % Stuarts_total)
    elif Stuarts_total < Kevins_total:
        print("Kevin %d" % Kevins_total)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)