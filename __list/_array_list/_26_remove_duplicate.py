class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        if l <= 1:
            return l
        count = 1
        tmp = nums[0]
        pos = 1
        for i in range(1,len(nums)):
            nums[pos] = nums[i]
            pos += 1
            if nums[i] != tmp:
                tmp = nums[i]
                nums[count] = nums[i]
                count += 1
        return count



so = Solution()
a = [1,1,2,2,3,3,3,3,4]
b = so.removeDuplicates(a)
print b
print a
