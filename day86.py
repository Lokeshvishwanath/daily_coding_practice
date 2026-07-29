# day25_search_rotated_sorted_array.py

class Solution:

    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


def main():

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    solution = Solution()

    index = solution.search(nums, target)

    print("Array :", nums)
    print("Target:", target)
    print("Index :", index)


if __name__ == "__main__":
    main()