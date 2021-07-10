class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rtype = []
        for num in range(numRows):
            tmp = []
            for idx in range(num+1):
                if idx == 0 or idx == num:
                    tmp.append(1)
                else:
                    tmp.append(rtype[num-1][idx]+rtype[num-1][idx-1])
            rtype.append(tmp)
        return rtype


s = Solution()
result = s.generate(5)
print(result)
