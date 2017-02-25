class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {}
        l = len(nums)
        for i in range(l):
            hm[nums[i]] = i
        for i in range(l):
            if nums[i] + nums[i] == target:
                if self.sp(nums,nums[i]) != -1:
                    return [i,self.sp(nums,nums[i])]
            if target-nums[i] in hm:
                t = hm[target-nums[i]]
                m = hm[nums[i]]
                if hm[target-nums[i]] != hm[nums[i]]:
                    return [i,hm[target-nums[i]]]

    def sp(self,nums,x):
        flag = False
        l = len(nums)
        for i in range(l):
            if nums[i] == x and flag == True:
                return i
            if nums[i] == x and flag == False:
                flag = True

        return -1



so = Solution()
a = [3,3]
tar = 6
x = so.twoSum(a,tar)
print x