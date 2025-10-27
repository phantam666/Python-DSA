from itertools import combinations

def print_combinations(s, k):
    # Sort the string to ensure lexicographic order
    sorted_string = ''.join(sorted(s))
    
    # Generate combinations of size 1 to k
    for size in range(1, k + 1):
        for combo in combinations(sorted_string, size):
            print(''.join(combo))

# Example usage
input_data = input()
s, k = input_data.split()
k = int(k)  # Convert k to an integer
print_combinations(s, k)
