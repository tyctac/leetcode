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
        target = 0
        margin = sys.maxint
        for i in range(l-2):
            j = i+1
            k = l-1
            if i>0 and nums[i] == nums[i-1]:
                continue
            k = l-1
            while j<k:
                if nums[i] + nums[j] +nums[k] < target:
                    if abs(nums[i] + nums[j] +nums[k] - target) < margin:
                        margin = abs(nums[i] + nums[j] +nums[k])
                    j +=1
                    while nums[j] == nums[j-1] and j<k:
                        j +=1
                elif nums[i] + nums[j] + nums[k] > target:
                    k = k -1
                    while nums[k] == nums[k+1] and k>j:
                        k = k -1
                else :
                    result.append([nums[i],nums[j],nums[k]])
                    j = j +1
                    k = k-1
                    while nums[j] == nums[j-1] and nums[k] == nums[k+1] and j<k:
                        j = j+1

        return result
so = Solution()
S = [-2,0,1,1,2]
x = so.threeSum(S)
print x
