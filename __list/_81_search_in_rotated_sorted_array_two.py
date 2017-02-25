# encoding=utf-8
# -,- 回头理解清楚一下
class Solution(object):
    def recur_search(self, left, right, nums, target):
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        if nums[mid] == nums[left]:
            tmp = mid
            while nums[tmp] == nums[left] and tmp > left:
                tmp = tmp -1
            if tmp == left:
                return self.recur_search(mid+1,right,nums,target)
            else: mid = tmp
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[left]:
            if target >= nums[left] or target < nums[mid]:
                return self.recur_search(left, mid - 1, nums, target)
            else:
                return self.bin_search(mid + 1, right, nums, target)
        if target >= nums[left] and target < nums[mid]:
            return self.bin_search(left, mid - 1, nums, target)
        else:
            return self.recur_search(mid + 1, right, nums, target)

    def bin_search(self, left, right, nums, target):
        if target < nums[left] or target > nums[right]:
            return -1
        if left == right:
            if nums[left] == target:
                return left
            else:
                return False
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.bin_search(left, mid - 1, nums, target)
        else:
            return self.bin_search(mid + 1, right, nums, target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return False
        x = self.recur_search(0, len(nums) - 1, nums, target)
        if x >= 0:
            print x
            return True
        else: return False

if __name__ == '__main__':
    so = Solution()
    a = [1,3,1]
    tar = 2
    print so.search(a,tar)
