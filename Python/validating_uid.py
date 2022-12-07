import re

T = int(input())

for _ in range(T):
    test_case = input()
    test_1 = re.search(r'([A-Z].*){2}', test_case)
    test_2 = re.search(r'([0-9].*){3}', test_case)
    test_3 = re.fullmatch(r'^[0-9a-zA-Z]{10}$', test_case)
    test_4 = len(set(test_case)) == 10

    if test_1 and test_2 and test_3 and test_4:
        print('Valid')
    else:
        print('Invalid')
