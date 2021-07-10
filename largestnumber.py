class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = -1
        maxIndex = -1
        for index in range(len(nums)):
            if nums[index] >= (max * 2):
                maxIndex = index
            elif nums[index] > (max / 2):
                maxIndex = -1
            if max < nums[index]:
                max = nums[index]
        return maxIndex
