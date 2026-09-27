# day50_maximum_product_subarray.py

class Solution:

    def max_product(self, nums):

        current_max = nums[0]
        current_min = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            # Store old values before changing them
            old_max = current_max
            old_min = current_min

            current_max = max(
                num,
                num * old_max,
                num * old_min
            )

            current_min = min(
                num,
                num * old_max,
                num * old_min
            )

            result = max(result, current_max)

        return result


def main():

    nums = [2, 3, -2, 4]

    solution = Solution()

    result = solution.max_product(nums)

    print("Array:", nums)
    print("Maximum Product:", result)


if __name__ == "__main__":
    main()