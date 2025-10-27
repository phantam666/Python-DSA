from collections import defaultdict

# Step 1: Read sizes
n, m = map(int, input().split())

# Step 2: Read group A and store positions
group_A = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    group_A[word].append(i)

# Step 3: Read group B and query group A
for _ in range(m):
    query = input().strip()
    if query in group_A:
        print(' '.join(map(str, group_A[query])))
    else:
        print(-1)
