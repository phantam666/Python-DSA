M = int(input())
a = list(map(int, input().split()))
N = int(input())
b= list(map(int, input().split()))

common = set(a) & set(b)

marge = a + b

result = [x for x in marge if x not in common]

print(result)