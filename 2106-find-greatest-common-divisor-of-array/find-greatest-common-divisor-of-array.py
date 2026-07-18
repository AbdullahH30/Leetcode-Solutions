from math import gcd
class Solution:
    def findGCD(self, nums: List[2,5,6,9,10]) -> int:
        smallest = min(nums)
        greatest = max(nums)
        return gcd(smallest,greatest)