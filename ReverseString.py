class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # start = 0
        # end = len(s) - 1
        # result=[]
        result = list(s)
        start = 0
        end = len(result)-1
        while start < end:
            result[start], result[end] = result[end], result[start]
            start += 1
            end -= 1
        return ''.join(result)


s = Solution()
result = s.reverseString("A man, a plan, a canal: Panama")
print(result)
