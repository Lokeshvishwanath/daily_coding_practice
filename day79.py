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

# day19A_maximum_product_subarray.py

class Solution:

    def max_product(self, nums):

        max_product = nums[0]
        min_product = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):

            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])

            answer = max(answer, max_product)

        return answer


def main():

    nums = [2, 3, -2, 4]

    solution = Solution()

    result = solution.max_product(nums)

    print("Array :", nums)
    print("Maximum Product:", result)


if __name__ == "__main__":
    main()