from math import gcd

class Solution:
    def gcdOfOddEvenSums(self, n):
        sumodd = n * n
        sumeven = n * (n + 1)
        return gcd(sumodd, sumeven)