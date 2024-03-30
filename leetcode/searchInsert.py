class Solution:
    def searchInsert(nums: list, target: int) -> int:
        start = 0
        final = len(nums) - 1

        while start <= final:
            mid = (start + final) // 2

            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                final = mid - 1
            else:
                return mid
        return final

lista = [1,3,5,6]

a = Solution.searchInsert(lista, 5)
print(a)