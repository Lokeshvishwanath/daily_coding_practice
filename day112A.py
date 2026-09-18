# day46_subarray_sum_equals_k.py

class Solution:

    def subarray_sum(self, nums, k):

        prefix_sum = 0
        count = 0

        prefix_count = {
            0: 1
        }

        for num in nums:

            prefix_sum += num

            needed = prefix_sum - k

            if needed in prefix_count:
                count += prefix_count[needed]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count


def main():

    nums = [1, 1, 1]
    k = 2

    solution = Solution()

    result = solution.subarray_sum(nums, k)

    print("Array:", nums)
    print("K:", k)
    print("Number of Subarrays:", result)


if __name__ == "__main__":
    main()