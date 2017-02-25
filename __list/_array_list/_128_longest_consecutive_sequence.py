class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {}
        for u in nums:
            hm[u] = True
        longest = 1
        for u in nums:
            tmp = u
            tmp_longest = 1
            while tmp +1 in hm:
                tmp_longest +=1
                tmp +=1
            tmp = u
            while tmp-1 in hm:
                tmp_longest += 1
                tmp -=1
            if tmp_longest > longest:
                longest = tmp_longest
        return longest

if __name__ == '__main__':
    nums1 = [1,2,3,53,52,54,51]
    so = Solution()
    print so.longestConsecutive(nums1)