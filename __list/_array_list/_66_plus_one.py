class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        all0 = True
        all9 = True
        l = len(digits)
        for i in digits:
            if i != 9 and all9 == True:
                all9 = False
            if i != 0 and all0 == True:
                all0 = False
        if all0 == True:
            return [1]
        if all9 == True:
            ret = [1]
            for i in range(l):
                ret.append(0)
            return ret

        b = range(l)
        b.reverse()
        c = 0
        cot = 1
        for i in b:
            x = digits[i] + cot
            cot = x/10
            digits[i] = x%10
        return digits

so = Solution()
a = [9,9,9]
b = so.plusOne(a)
print b

