# day53_contains_duplicate.py

class Solution:

    def contains_duplicate(self, nums):

        seen = set()

        for num in nums:

            if num in seen:
                return True

            seen.add(num)

        return False


def main():

    nums = [1, 2, 3, 1]

    solution = Solution()

    result = solution.contains_duplicate(nums)

    print("Array:", nums)
    print("Contains Duplicate:", result)


if __name__ == "__main__":
    main()