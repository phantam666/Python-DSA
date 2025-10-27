class Solution:

    def findSum(self, s1, s2):
        # Before proceeding further,
        # make sure length of s2 is larger.
        if (len(s1) > len(s2)):
            t = s1
            s1 = s2
            s2 = t

        # Take an empty string for
        # storing result
        str = ""

        # Calculate length of both string
        n1 = len(s1)
        n2 = len(s2)

        # Reverse both of strings
        s1 = s1[::-1]
        s2 = s2[::-1]

        carry = 0
        for i in range(n1):

            # Do school mathematics, compute
            # sum of current digits and carry
            sum = ((ord(s1[i]) - 48) + ((ord(s2[i]) - 48) + carry))
            str += chr(sum % 10 + 48)

            # Calculate carry for next step
            carry = int(sum / 10)

        # Add remaining digits of larger number
        for i in range(n1, n2):
            sum = ((ord(s2[i]) - 48) + carry)
            str += chr(sum % 10 + 48)
            carry = (int)(sum / 10)

        # Add remaining carry
        if (carry):
            str += chr(carry + 48)

        # reverse resultant string
        str = str[::-1]

        i = 0
        n = len(str)
        while i < n and str[i] == '0':
            i += 1

        if i == n:
            return "0"

        return str[i:]
    
obj = Solution()
print(obj.findSum("123", "456"))  # Output: "579"