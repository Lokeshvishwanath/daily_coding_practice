# day35_move_zeroes.py

class Solution:

    def move_zeroes(self, nums):

        non_zero = 0

        for i in range(len(nums)):

            if nums[i] != 0:

                nums[non_zero] = nums[i]

                non_zero += 1

        for i in range(non_zero, len(nums)):

            nums[i] = 0

        return nums


def main():

    nums = [0, 1, 0, 3, 12]

    solution = Solution()

    result = solution.move_zeroes(nums)

    print("Original Array: [0, 1, 0, 3, 12]")
    print("After Moving Zeroes:", result)


if __name__ == "__main__":
    main()