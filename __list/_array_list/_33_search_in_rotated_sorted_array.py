class Solution(object):

    def recur_search(self,left,right,nums,target):
        if left == right:
            if nums[left] == target:
                return left
            else :
                return -1
        mid = (left + right)/2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[left]:
            if target >= nums[left] or target < nums[mid]:
                return self.recur_search(left, mid - 1, nums, target)
            else: return self.bin_search(mid+1,right,nums,target)
        if target >= nums[left] and target < nums[mid]:
            return self.bin_search(left,mid-1,nums,target)
        else:
            return self.recur_search(mid+1,right,nums,target)

    def bin_search(self,left,right,nums,target):
        if target < nums[left] or target > nums[right]:
            return -1
        if left == right:
            if nums[left] == target:
                return left
            else: return -1
        mid = (left + right)/2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.bin_search(left,mid-1,nums,target)
        else: return self.bin_search(mid+1,right,nums,target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return

if __name__ == '__main__':
    so = Solution()
    a = [7,8,9,99,1,3,5,6]
    b = so.recur_search(0,len(a)-1,a,6)
    print b
