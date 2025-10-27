from itertools import combinations_with_replacement

def print_combinations(s, k):
    # Sort the string to ensure lexicographic order
    sorted_s = ''.join(sorted(s))
    # Generate combinations_with_replacement of size 1 to k
    for combo in combinations_with_replacement(sorted_s, k):
        print(''.join(combo))

# Example usage
input_data = input()
s, k = input_data.split()
k = int(k)  # Convert k to an integer
print_combinations(s, k)
