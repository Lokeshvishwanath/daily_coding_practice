# day19_maximum_subarray_sum.py

class Solution:

    def max_subarray(self, nums):

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):

            current_sum = max(nums[i], current_sum + nums[i])

            max_sum = max(max_sum, current_sum)

        return max_sum


def main():

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    solution = Solution()

    result = solution.max_subarray(nums)

    print("Array:", nums)
    print("Maximum Subarray Sum:", result)


if __name__ == "__main__":
    main()