def findSmallestInteger(nums, value):
    remainder_count = {}
    for num in nums:
        remainder = num % value
        if remainder < 0:
            remainder += value
        if remainder in remainder_count:  
            remainder_count[remainder] += 1
        else:
            remainder_count[remainder] = 1

    missing_integer = 0
    while True:
        remainder = missing_integer % value
        if remainder < 0:
            remainder += value
        if remainder in remainder_count and remainder_count[remainder] > 0:
            remainder_count[remainder] -= 1
        else:
            return missing_integer
        missing_integer += 1
 

nums = [1,-10,7,13,6,8]
value = 5 
print(findSmallestInteger(nums, value))