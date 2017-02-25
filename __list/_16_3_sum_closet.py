import sys
class Solution(object):

    def threeSumClosest(self, nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l = len(nums)
        result = []
        margin = sys.maxint
        result =1
        for i in range(l-2):
            j = i+1
            k = l-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            k = l-1
            while j<k:
                if nums[i] + nums[j] +nums[k] < target:
                    if abs(nums[i] + nums[j] +nums[k] - target) < margin:
                        margin = abs(nums[i] + nums[j] +nums[k] - target)
                        result = nums[i] + nums[j] +nums[k]
                    j +=1
                    while nums[j] == nums[j-1] and j<k:
                        j +=1
                elif nums[i] + nums[j] + nums[k] > target:
                    if abs(nums[i] + nums[j] +nums[k] - target) < margin:
                        margin = abs(nums[i] + nums[j] +nums[k] - target)
                        result = nums[i] + nums[j] +nums[k]
                    k = k -1
                    while nums[k] == nums[k+1] and k>j:
                        k = k -1
                else :
                    return nums[i]+nums[j]+nums[k]

        return result
so = Solution()
S = [1,1,1,0]
t = 100
x = so.threeSumClosest(S,3)
print x
