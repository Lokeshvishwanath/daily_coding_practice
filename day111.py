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



# day45_longest_subarray_sum_k.py

class Solution:

    def longest_subarray(self, nums, k):

        prefix_sum = 0
        max_length = 0

        first_index = {
            0: -1
        }

        for i in range(len(nums)):

            prefix_sum += nums[i]

            needed = prefix_sum - k

            if needed in first_index:

                length = i - first_index[needed]

                max_length = max(max_length, length)

            if prefix_sum not in first_index:

                first_index[prefix_sum] = i

        return max_length


def main():

    nums = [10, 5, 2, 7, 1, 9]
    k = 15

    solution = Solution()

    result = solution.longest_subarray(nums, k)

    print("Array:", nums)
    print("K:", k)
    print("Longest Length:", result)


if __name__ == "__main__":
    main()