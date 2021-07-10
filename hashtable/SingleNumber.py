class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index, item in enumerate(nums):
            if item == 1:
                continue
            for otherIndex, otherItem in enumerate(nums[index+1:]):
                if item == otherItem:
                    return otherIndex + index+1
        return -1


s = Solution()
result = s.singleNumber([4, 1, 2, 1, 2])
print(result)
