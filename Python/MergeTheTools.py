from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    substring_list = list(map(''.join, zip(*[iter(string)]*k)))
    filtered_substrings = list(map(lambda x: ''.join(OrderedDict.fromkeys(x)), substring_list))
    return print(*filtered_substrings,sep='\n')

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
