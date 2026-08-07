# day28A_single_element_sorted_array.py

class Solution:

    def single_non_duplicate(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


def main():

    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

    solution = Solution()

    result = solution.single_non_duplicate(nums)

    print("Array :", nums)
    print("Single Element:", result)


if __name__ == "__main__":
    main()