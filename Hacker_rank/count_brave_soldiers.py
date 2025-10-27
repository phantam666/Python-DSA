def count_brave_soldiers(n):
    count = 0
    num = 2
    while True:
        is_prime = True
        for i in range (2, (num**0.5)+1):
             if num % i == 0:
                 is_prime = False
                 break
        if is_prime:
            square = num*num
            if square > n:
                 break
        count += 1
        num += 1
    return count

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())  # The input contains only one integer N

    # Call the user logic function and print the output
    result = count_brave_soldiers(n)
    print(result)

if __name__ == "__main__":
    main()