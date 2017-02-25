class Solution(object):

    def findKth(self,nums1,l1,r1,nums2,l2,r2,k):
        if (r1-l1+1) > (r2-l2+1):
            return self.findKth(nums2,l2,r2,nums1,l1,r1,k)
        if (r1-l1+1) == 0:
            return nums2[l2+k-1]
        if k == 1:
            return min(nums1[l1],nums2[l2])
        pa = min(k/2,r1-l1+1)
        pb = k - pa
        if nums1[l1+pa-1] < nums2[l2+pb-1]:
            return self.findKth(nums1,l1+pa,r1,nums2,l2,r2,k-pa)
        else:
            return self.findKth(nums1,l1,r1,nums2,l2+pb,r2,k-pb)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1);len2 = len(nums2)
        total = len1 + len2
        if total%2 == 1:
            return self.findKth(nums1,0,len1-1,nums2,0,len2-1,total/2+1)
        else :
            return (self.findKth(nums1,0,len1-1,nums2,0,len2-1,total/2) + self.findKth(nums1,0,len1-1,nums2,0,len2-1,total/2+1))/2.0

if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]
    so = Solution()
    print so.findMedianSortedArrays(nums1,nums2)