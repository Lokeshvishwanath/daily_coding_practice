# day44_minimum_size_subarray_sum.py

class Solution:

    def min_subarray_len(self, target, nums):

        left = 0
        window_sum = 0
        min_length = float("inf")

        for right in range(len(nums)):

            window_sum += nums[right]

            while window_sum >= target:

                length = right - left + 1

                min_length = min(min_length, length)

                window_sum -= nums[left]
                left += 1

        if min_length == float("inf"):
            return 0

        return min_length


def main():

    target = 7
    nums = [2, 3, 1, 2, 4, 3]

    solution = Solution()

    result = solution.min_subarray_len(target, nums)

    print("Target:", target)
    print("Array:", nums)
    print("Minimum Length:", result)


if __name__ == "__main__":
    main()