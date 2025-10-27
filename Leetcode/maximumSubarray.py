def maximumsubarray(arr):
    if len(arr) == 0:
        return arr[0] 
    current_max = arr[0]
    max_so_far = arr[0]
    
    for i in range(len(arr)):
        
        current_max = max(arr, current_max + arr)
        max_so_far = max(max_so_far, current_max)
    return max_so_far

# Example usage:
arr = [1,2,-1,3,4,-2,6]
print(maximumsubarray(arr))  # Output: 6