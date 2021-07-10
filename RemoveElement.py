class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for item in nums:
            if item != val:
                nums[k] = item
                k += 1
        return k


s = Solution()
result = s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(result)
