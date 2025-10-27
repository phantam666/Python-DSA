M = int(input())
a = list(input().split())

# Use a set to remove duplicates
unique_countries = set(a)

# Count the unique values
print(len(unique_countries))