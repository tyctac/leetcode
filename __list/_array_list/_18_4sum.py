class Solution(object):

    def set_tp4s(self,set1,set2,tp4s):
        for i in set1:
            tmset = set()
            tmset.add(i[0])
            tmset.add(i[1])
            for j in set2:
                tmset2 = set()
                tmset2.add(j[0])
                tmset2.add(j[1])
                if len(tmset2.union(tmset)) == 4:
                    tp4s.add(tuple(tmset2.union(tmset)))

    def get_real_tp4s(self,tp4s,nums):
        rtp4s = set()
        for i in tp4s:
            tmp_list = []
            for n in i:
                tmp_list.append(nums[n])
            tmp_list.sort()
            if tuple(tmp_list) not in rtp4s:
                rtp4s.add(tuple(tmp_list))
        return rtp4s

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sum_node_set = {}
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                s = nums[i] + nums[j]
                tp = (i, j)
                if s in sum_node_set:
                    sum_node_set[s].add(tp)
                else:
                    sum_node_set[s] = set()
                    sum_node_set[s].add(tp)
        tp4s = set()
        for sm in sum_node_set:
            if sm == -3:
                print '-3'
            dif = target - sm
            if dif not in sum_node_set:
                continue
            self.set_tp4s(sum_node_set[sm],sum_node_set[dif],tp4s)
        rtp4s = self.get_real_tp4s(tp4s,nums)
        ret = []
        for i in rtp4s:
            ret.append(list(i))
        print ret
        ret=sorted(ret,cmp = cmp2)
        return ret


def cmp2(l1,l2):
    if l1[0] != l2[0]:
        return l1[0]-l2[0]
    elif l1[1] != l2[1]:
        return l1[1]-l2[1]
    elif l1[2] != l2[2]:
        return l1[2]-l2[2]
    else :
        return l1[3]-l2[3]

so = Solution()
S = [-4,-3,-2,-1,0,0,1,2,3,4]
target = 0
tmp = so.fourSum(S,target)

print tmp