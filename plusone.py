class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits[0] += 1
        up = 0
        for idx, item in enumerate(digits):
            digits[idx] = item + up
            if digits[idx] >= 10:
                up = digits[idx] // 10
                digits[idx] = digits[idx] % 10
            else:
                up = 0
                break
        if(up != 0):
            digits.append(up)
        digits.reverse()
        return digits


so = Solution()
result = so.plusOne([1, 2, 9])
print(result)
# solution = new Solution()
# result = solution.plusOne([1, 2, 3])
# print(result)
