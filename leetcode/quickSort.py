class Solution:
    def quickSorty(nums: list) -> list:
        highest = []
        lowest = []

        for i in range(len(nums)):
            mid = len(nums) // 2
            pivot = nums[-1]

            if nums[i] < pivot:
                lowest.append(nums[i])
            elif nums[i] > pivot:
                highest.append(nums[i])

        nums = []
        nums.extend(highest)
        nums.extend(lowest)

        print(nums)
        print(lowest)
        print(highest)


x = [9, -3, 5, 2, 6, 8, -6, 1, 3]
print(x)
print(Solution.quickSorty(x))