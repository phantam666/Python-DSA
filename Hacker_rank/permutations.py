from itertools import permutations

s, k = input().split()
k = int(k)
sorted_s = sorted(s.upper())
print("\n".join (sorted_s))
for p in permutations(sorted_s, k):
    print(''.join(p))