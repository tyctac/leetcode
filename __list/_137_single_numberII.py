import sys
import math
class Solution(object):
    def singleNumber(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        int_size = sys.getsizeof(int())
        l = len(nums)
        count = []
        for i in range(int_size):
            count.append(0)
        for i in range(l):
            for j in range(int_size):
                if nums[i] & (int)(math.pow(2,j)) == (int)(math.pow(2,j)):
                    count[j] +=1
        s = 0
        for j in range(int_size):
            if count[j] % 3 != 0:
                count[j] = count[j] % 3
            else:
                count[j] = 0
        if count[int_size-1] == 0:
            for j in range(int_size):
                if count[j] % 3 != 0:
                    s += math.pow(2,j)
        else:
            s = 0
            for j in range(int_size):
                count[j] = 1 - count[j]
            for j in range(int_size):
                if count[j] %3 != 0:
                    s += math.pow(2,j)
            s = 0-(s+1)
        return (int)(s)


    def singleNumber_old(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        dic = {}
        for i in range(l):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] +=1
        for x in dic:
            if dic[x] == 1:
                return x


so = Solution()
a = [1,1,1,3,4,4,4]
b = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
c = [43,16,45,89,45,-2147483648,45,2147483646,-2147483647,-2147483648,43,2147483647,-2147483646,-2147483648,89,-2147483646,89,-2147483646,-2147483647,2147483646,-2147483647,16,16,2147483646,43]
print so.singleNumber(c)
