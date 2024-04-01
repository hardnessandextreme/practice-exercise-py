from typing import List


class Solution:
    @staticmethod
    def findRightInterval(intervals: list[list[int]]) -> list[list[int]]:
        return sorted(intervals, key=lambda x: x[0])


print(Solution.findRightInterval([[1,2],[7,6],[8,2]]))