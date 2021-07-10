class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return -1
        tmp = 0
        alters = []
        for item in nums:
            tmp += item
            alters.append(tmp)
        total = alters[len(alters)-1]
        for idx, item in enumerate(nums):
            if total - alters[idx] == alters[idx] - item:
                return idx
        return -1


nums = [1, 7, 3, 6, 5, 6]
result = Solution()
pivotIndex = result.pivotIndex(nums)
print(pivotIndex)
