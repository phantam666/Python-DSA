def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

i = int(input("Enter the Number : "))
print(sum(i))