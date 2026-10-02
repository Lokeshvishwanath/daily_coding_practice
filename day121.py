# day54_two_sum.py

class Solution:

    def two_sum(self, nums, target):

        seen = {}

        for i in range(len(nums)):

            current = nums[i]

            needed = target - current

            if needed in seen:
                return [seen[needed], i]

            seen[current] = i

        return []


def main():

    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()

    result = solution.two_sum(nums, target)

    print("Array:", nums)
    print("Target:", target)
    print("Indices:", result)


if __name__ == "__main__":
    main()