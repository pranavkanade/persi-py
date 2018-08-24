def count_substring(string, sub_string):
    l = 0
    ls = len(sub_string)
    for i in range(len(string)):
        if string[i:i+ls] == sub_string:
            l +=1
    return l

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)