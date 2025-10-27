class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        present_row = 0
        going_down = False

        for c in s:
            rows[present_row] += c
            if present_row == 0 or present_row == numRows - 1:
                going_down = not going_down
            present_row += 1 if going_down else -1

        return "".join(rows)

# Example usage
s = "PAYPALISHIRING"
numRows = 5
sol = Solution()
result = sol.convert(s, numRows)
print(result)
