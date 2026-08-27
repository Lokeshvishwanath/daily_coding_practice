# day36A_squares_sorted_array.py

class Solution:

    def sorted_squares(self, nums):

        n = len(nums)

        result = [0] * n

        left = 0
        right = n - 1

        position = n - 1

        while left <= right:

            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:

                result[position] = left_square
                left += 1

            else:

                result[position] = right_square
                right -= 1

            position -= 1

        return result


def main():

    nums = [-4, -1, 0, 3, 10]

    solution = Solution()

    result = solution.sorted_squares(nums)

    print("Original Array:", nums)
    print("Sorted Squares:", result)


if __name__ == "__main__":
    main()