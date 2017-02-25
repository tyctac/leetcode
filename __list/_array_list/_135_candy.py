class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        l = len(ratings)
        increment = []
        for i in range(l):
            increment.append(1)
        inc = 1
        for i in range(1,l):
            if ratings[i] > ratings[i-1]:
                increment[i] = increment[i-1]+1
        b = range(l)
        b.reverse()
        for i in range(1,l):
            if ratings[b[i]] > ratings[b[i-1]]:
                increment[b[i]] = max(increment[b[i]],increment[b[i-1]]+1)
        return sum(increment)


so = Solution()
ra = [1,3,4,2,7,5]
rb = [1,2,2]
rc = [1,0,2]
rd = [4,2,3,4,1]
print so.candy(rd)
