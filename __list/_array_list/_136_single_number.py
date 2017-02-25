class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = nums[0]
        l = len(nums)
        for i in range(1,l):
            x = x ^ nums[i]
        return x