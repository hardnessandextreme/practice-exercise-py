class Solution:
    @staticmethod
    def nextGreatestLetter(letters: list[str], target: str) -> str:
        start = 0
        final = len(letters) - 1

        while start <= final:
            mid = (start + final) // 2

            if target < letters[mid]:
                final = mid - 1
            else:
                start = mid + 1
        return letters[start % len(letters)]

a = ["c", "f", "j"]
b = "c"

print(Solution.nextGreatestLetter(a, b))