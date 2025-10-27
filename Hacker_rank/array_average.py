def average(array):
 total = sum(array)
 count = len(array)
 return float(total/count)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)