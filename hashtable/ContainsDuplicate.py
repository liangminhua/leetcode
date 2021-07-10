class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        setLength = len(hashset)
        for item in nums:
            hashset.add(item)
            if len(hashset) > setLength:
                setLength += 1
            else:
                return True
        return False
            # if len(nums) == len(hashset):
            #     return False
            # else:
            #     return True
