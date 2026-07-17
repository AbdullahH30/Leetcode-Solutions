from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        maxVal = max(nums)
        freq = [0] * (maxVal + 1)
        for x in nums:
            freq[x] += 1

        cntDiv = [0] * (maxVal + 1)
        for d in range(1, maxVal + 1):
            for multiple in range(d, maxVal + 1, d):
                cntDiv[d] += freq[multiple]

        exact = [0] * (maxVal + 1)

        for d in range(maxVal, 0, -1):
            c = cntDiv[d]
            exact[d] = c * (c - 1) // 2

            multiple = 2 * d
            while multiple <= maxVal:
                exact[d] -= exact[multiple]
                multiple += d

        prefix = []
        values = []

        running = 0
        for g in range(1, maxVal + 1):
            if exact[g]:
                running += exact[g]
                values.append(g)
                prefix.append(running)

        ans = []
        for q in queries:
            idx = bisect_right(prefix, q)
            ans.append(values[idx])

        return ans