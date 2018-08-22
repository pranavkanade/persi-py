def merge_the_tools(string, k):
    # print(len(string))
    num_of_sub_str = len(string)//k
    # print(num_of_sub_str)
    sub_strs = [string[i*k:i*k+k]   # follow this k very well
                for i in range(num_of_sub_str)]
    # instrumentation
    # print(sub_strs)

    for each_str in sub_strs:
        new_str = ''
        for e in each_str:
            if e not in new_str:
                new_str += e
        print(new_str)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)