class Solution:
    @staticmethod
    def searchRange(nums: list[int], target: int) -> list[int]:

        def first(nums, target):
            for num in range(len(nums)):
                if nums[num] == target:
                    return num
            return -1

        def last(nums, target):
            for num in range(len(nums)-1, -1, -1):
                if nums[num] == target:
                    return num
            return -1

        f, l = first(nums,target), last(nums, target)
        return [f,l]

a = [5,7,7,8,8,10]
target = 6

print(Solution.searchRange(a, target))