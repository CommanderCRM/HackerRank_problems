from itertools import combinations

n = int(input())
n_array = list(input().split())
k = int(input())

indices = tuple(range(1, n+1))
a_indices = tuple(i+1 for i, x in enumerate(n_array) if x == 'a')

combos = list(combinations(indices, k))
length = len(combos)
count = 0

for combo in combos:
    for a in a_indices:
        if a in combo:
            count += 1
            break

print(count/length)
