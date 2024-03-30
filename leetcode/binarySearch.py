class Solution:
    def search(nums: list, target: int) -> int:
        """
        :param nums: Sorted list of integers
        :param target: Number to be found in the list
        :return: Index of the target number in the list
        """
        start = 0
        final = len(nums) - 1

        while start <= final:
            mid = (start + final) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                final = mid - 1
        return -1

x = range(3,10)
lista = list(x)

print(lista)

asd = Solution.search(lista, 5)

if asd == -1:
    print("Element not found")
else:
    print(asd)