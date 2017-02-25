import math
class Solution(object):
    def climbStairs(self,n):
        s = math.sqrt(5.0)
        return math.floor((math.pow((1+s)/2,n+1) + math.pow((1-s)/2,n+1))/s+0.5)


    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)