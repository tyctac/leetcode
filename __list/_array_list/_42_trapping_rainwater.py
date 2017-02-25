class Solution(object):
    def get_max_index(self,height,left,right):
        ma = -1
        index = -1
        for i in range(left+1,right):
            if height[i] > ma:
                ma = height[i]
                index = i
        return index

    def make_convex(self,height,con_dic,left,right):
        if left + 1 == right:
            return
        if height[left] <= height[right]:
            up = True
        else :
            up = False
        if up == True:
            mi = self.get_max_index(height,left,right)
            if height[left] < height[right]:
                min = height[left]
            else:
                min = height[right]
            if height[mi] <= height[left]:
                con_dic[left] = min
                con_dic[right] = min
                return
            self.make_convex(height,con_dic,left,mi)
            self.make_convex(height, con_dic, mi, right)
        else:
            mi = self.get_max_index(height, left, right)
            if height[left] < height[right]:
                min = height[left]
            else:
                min = height[right]
            if height[mi] <= height[right]:
                con_dic[left] = min
                con_dic[right] = min
                return
            self.make_convex(height, con_dic, left, mi)
            self.make_convex(height, con_dic, mi, right)
        return

    def get_water(self,height,con_dic):
        l = len(height)
        broad = []
        tmpleft = 0
        tmpright = l-1
        j1 = 0
        for i in range(l):
            if con_dic[i] != -1:
                j1 = i
                break
        j2 = l-1
        b = range(l)
        b.reverse()
        for i in b:
            if con_dic[i] != -1:
                j2 = i
                break
        for i in range(j1,j2+1):
            tmpdic = {}
            tmpdic['right'] = -1
            if con_dic[i] == -1:
                tmpdic['left'] = tmpleft
            else:
                tmpleft = i
                tmpdic['left'] = tmpleft
            broad.append(tmpdic)
        b = range(j1,j2+1)
        b.reverse()
        for i in b:
            if con_dic[i] == -1:
                broad[i]['right'] = tmpright
            else:
                tmpright = i
                broad[i-j1]['right'] = tmpright
        k = 0
        sum = 0
        print broad
        for i in range(j1,j2+1):
            lef = broad[k]['left']
            rig = broad[k]['right']
            k = k + 1
            if lef == rig:
                continue
            m = min(height[lef],height[rig])
            sum += max(m - height[i],0)

            # use_list.append(m)
        return sum



    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        if len(height) == 0:
            return 0
        seq = range(len(height))
        con_dic = {}
        for i in seq:
            con_dic[i] = -1
        self.make_convex(height,con_dic,0,len(height)-1)
        print con_dic
        x = self.get_water(height,con_dic)
        return x

so = Solution()
hgt = [0,1,0,2,1,0,1,3,2,1,2,1]
h2 = [5,4,1,2]
h3 = [2,2,3,4,8,1,8]
h4 = [7,1,8,6,6,1,5,3]
h5 = [0,5,6,4,6,1,0,0,2,7]
print so.trap(h5)