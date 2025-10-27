class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        
        quotient = 0
        
        # Subtract divisor multiples from dividend
        while dividend_abs >= divisor_abs:
            temp = divisor_abs
            multiple = 1
            while dividend_abs >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend_abs -= temp
            quotient += multiple
        
        return -quotient if negative else quotient
