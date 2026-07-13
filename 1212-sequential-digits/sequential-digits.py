class Solution(object):
    def sequentialDigits(self, low=100, high=300):

        ans = []

        digits = "123456789"

        low_len = len(str(low))
        high_len = len(str(high))

        for length in range(low_len, high_len + 1):

            for start in range(0, 10 - length):

                num = int(digits[start:start + length])

                if low <= num <= high:
                    ans.append(num)

        return ans