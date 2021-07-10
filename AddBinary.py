class Solution:
    def getBit(self, str, index):
        if index > len(str) - 1:
            return '0'
        else:
            return str[len(str) - index - 1]

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        maxLength = max(len(a), len(b))
        idx = 0
        up = '0'
        while idx < maxLength or up == '1':
            aBit = self.getBit(a, idx)
            bBit = self.getBit(b, idx)
            if aBit == '1' and bBit == '1':
                result = up + result
                up = '1'
            elif aBit != bBit:
                if up == '1':
                    result = '0' + result
                    up = '1'
                else:
                    result = '1' + result
                    up = '0'
            else:
                result = up + result
                up = '0'
            print(idx, result, aBit, bBit, up)
            idx += 1
        return result


s = Solution()
result = s.addBinary("11", "1")
print(result)
