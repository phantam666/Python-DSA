N = int(input())
Num_strings = set(map(int, input().split()))
M = int(input())

for _ in range(M):
    command = input().split()
    if command[0] == "pop":
        if Num_strings:  # avoid KeyError if set is empty
            Num_strings.pop()
    elif command[0] == "remove":
        try:
            Num_strings.remove(int(command[1]))
        except KeyError:
            pass
    elif command[0] == "discard":
        Num_strings.discard(int(command[1]))

print(sum(Num_strings))

