from typing import List
import sys


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        tmp = {}
        for item in nums:
            for key in list(tmp.keys()):
                dic = abs(key-item)
                if dic < tmp[key]:
                    tmp[key] = dic
            tmp[item] = sys.maxsize
        print(tmp)
        return 1


s = Solution()

s.maximumGap([3, 6, 9, 1])
