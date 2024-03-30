class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:
        lista = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    lista = [j, i]

        return lista
