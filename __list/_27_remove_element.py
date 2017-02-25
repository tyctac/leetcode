class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        if l == 0:
            return 0
        c = range(l)
        c.reverse()
        for i in c:
            if nums[i] == val:
                del nums[i]
        return len(nums)

so = Solution()
a = [3,3]
so.removeElement(a,3)
print len(a)
print a