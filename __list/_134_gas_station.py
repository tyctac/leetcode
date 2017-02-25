class Solution(object):

    def canCompleteCircuit_old(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        left = []
        for i in range(l):
            left.append(gas[i] - cost[i])
        total = 0
        j = -1
        sum = 0
        for i in range(l):
            sum += left[i]
            total += left[i]
            if sum < 0:
                j = i
                sum = 0
        if total>=0:
            return j + 1
        else:
            return -1


    def canCompleteCircuit__complicate(self):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # l = len(gas)
        # left = []
        # for i in range(l):
        #     left.append(gas[i] - cost[i])
        left = [-1,1,1,2,-1,-3,4,-2]
        l  = len(left)
        ret_index = -1
        next1 = []
        sum1 = []
        for i in range(l):
            next1.append(i+1)
            sum1.append(left[i])
        can_go = True
        pos = 0
        count = 0
        flag = False
        while count < l :
            if flag == True:
                count += 1
            tpsum = left[pos]
            tpleft = pos
            pos2 = next1[pos]
            while sum1[pos2]*left[pos] > 0:
                tpsum += left[pos]
                next1[tpleft] = next1[pos2]
                pos = next1[pos2]
                pos2 = next1[pos]
            if left[pos2]*left[pos] < 0 and flag == False:
                flag = True
                pos = next1[pos]


        print left
        print next1
        print sum1






    def canCompleteCircuit_old(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        left = []
        for i in range(l):
            left.append(gas[i]-cost[i])

        ret_index = -1
        for i in range(l):
            current_gas = 0
            count = 1
            j = i
            while count<= l:
                current_gas += left[j]
                if current_gas < 0:
                    break
                count +=1
                j = (j+1)%l
            if current_gas < 0 :
                continue
            else :
                ret_index = i
                return ret_index
        return ret_index

so = Solution()
a , b = [5,3],[6,2]
x = so.canCompleteCircuit()


