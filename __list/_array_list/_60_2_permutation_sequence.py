class Solution(object):

    def get_factorial_list(self,k):
        li = []
        for i in range(1,k+1):
            sum = 1
            for j in range(1,i+1):
                sum *= j
            li.append(sum)
        return li


    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = range(n+1)
        nums = nums[1:]
        # for i in range(k):
        #     self.nextPermutation(nums)
        tmp_nums = []
        for x in nums:
            tmp_nums.append(x)
        ai_list = []
        l = len(nums)
        fact_list = self.get_factorial_list(l)
        fact_list.reverse()
        del fact_list[0]

        l_trim = len(tmp_nums)
        for i in range(l):
            if len(tmp_nums) == 1:
                ai_list.append(tmp_nums[0])
                break
            ai = (k-1)/fact_list[i]
            ai_list.append(tmp_nums[ai])
            del tmp_nums[ai]
            k = k - fact_list[i]*(ai+1)

        return ''.join([str(i) for i in ai_list])

so = Solution()
# print so.get_factorial_list(5)
print so.getPermutation(3,5)