import math
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        last = self.grayCode(n-1)
        l = len(last)
        # backpart = []
        i = l-1
        while i>=0:
            tmp = last[i]+math.pow(2,n-1)
            last.append((int)(tmp))
            i = i-1
        return last

so = Solution()
print so.grayCode(2)