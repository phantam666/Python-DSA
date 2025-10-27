from itertools import permutations

def print_permutations(s, k):
    
    perms = sorted(set((permutations(s, k))))
    for perm in perms:
        print(''.join(perm))

if __name__ == "__main__":
    s = input().upper()
    k = int(input())
    print_permutations(s, k)