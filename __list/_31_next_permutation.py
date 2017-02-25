class Solution(object):

    def reverse_part(self,nums,start,end):
        p2 = (end-start+1)/2
        for i in range(p2):
            tmp = nums[start+i]
            nums[start+i] = nums[end-i]
            nums[end-i] = tmp

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        rvs = range(l)
        rvs.reverse()
        pti = -1
        tmp = rvs[0]
        for i in rvs[1:]:
            if nums[i]>=nums[tmp]:
                tmp = i
            else:
                pti = i
                break
        if pti == -1:
            self.reverse_part(nums,0,l-1)
        chg = -1
        for i in rvs:
            if nums[i] > nums[pti]:
                chg = i
                break
        tmp = nums[pti]
        nums[pti] = nums[chg]
        nums[chg] = tmp
        self.reverse_part(nums,pti+1,l-1)
        # tplist = nums[pti+1:]
        # remain = nums[0:pti+1]
        # tplist.reverse()
        # remain.extend(tplist)
        # nums = remain
        print nums

so = Solution()
a = [5,1,1]
so.nextPermutation(a)