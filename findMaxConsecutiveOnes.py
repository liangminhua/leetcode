class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNumber = 0
        count = 0
        for x in nums:
            if x != 0:
                count = 1
            else:
                count += 1
                if count > maxNumber:
                    maxNumber = count
        return maxNumber
