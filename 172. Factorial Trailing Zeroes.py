class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n >= 5:
            res += n // 5
            n = n // 5
        return res
