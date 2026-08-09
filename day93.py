# day29_find_minimum_rotated_array.py

class Solution:

    def find_minimum(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:

                left = mid + 1

            else:

                right = mid

        return nums[left]


def main():

    nums = [4, 5, 6, 7, 0, 1, 2]

    solution = Solution()

    result = solution.find_minimum(nums)

    print("Array:", nums)
    print("Minimum Element:", result)


if __name__ == "__main__":
    main()


# day29A_two_sum_hashmap.py

class Solution:

    def two_sum(self, nums, target):

        seen = {}

        for i in range(len(nums)):

            current = nums[i]

            complement = target - current

            if complement in seen:
                return [seen[complement], i]

            seen[current] = i

        return []


def main():

    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()

    result = solution.two_sum(nums, target)

    print("Array :", nums)
    print("Target:", target)
    print("Indices:", result)


if __name__ == "__main__":
    main()