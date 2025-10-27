from collections import Counter

# Step 1: Get the number of shoes
total_shoes = int(input())  # We ignore this number, assuming we get the full list next

# Step 2: Get the available shoe sizes
shoe_sizes = list(map(int, input().split()))
inventory = Counter(shoe_sizes)

# Step 3: Get number of customer requests
customer_num = int(input())

# Step 4: Process each customer's request
total = 0
for _ in range(customer_num):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        total += price
        inventory[size] -= 1  # One shoe sold

# Step 5: Output total earnings
print(total)
