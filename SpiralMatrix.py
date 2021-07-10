from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        1,0,-1,
        m, n = len(matrix), len(matrix[0])
        size = m*n
        x, y, step = 0, 0, 1
        tmp = []
        while len(tmp) != size:
            while x < n and x >= 0:
                tmp.append(matrix[x][y])
                x += step
            while y < m and y >= 0:
                tmp.append(matrix[x][y])
                y += step
            step *= -1
        return tmp


matrix12 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

s = Solution()
result = s.spiralOrder(matrix12)
# print(result)
