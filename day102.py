# day35A_remove_duplicates.py

class Solution:

    def remove_duplicates(self, nums):

        if len(nums) == 0:
            return 0

        i = 0

        for j in range(1, len(nums)):

            if nums[j] != nums[i]:

                i += 1
                nums[i] = nums[j]

        return i + 1


def main():

    nums = [1, 1, 2, 2, 3, 3]

    solution = Solution()

    k = solution.remove_duplicates(nums)

    print("Unique Count:", k)
    print("Unique Elements:", nums[:k])


if __name__ == "__main__":
    main()