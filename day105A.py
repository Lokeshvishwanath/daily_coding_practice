# day37A_two_sum_sorted.py

class Solution:

    def two_sum(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]

            elif total < target:
                left += 1

            else:
                right -= 1

        return []


def main():

    numbers = [2, 7, 11, 15]
    target = 9

    solution = Solution()

    result = solution.two_sum(numbers, target)

    print("Numbers:", numbers)
    print("Target:", target)
    print("Answer:", result)


if __name__ == "__main__":
    main()


class Solution:

    def three_sum(self, nums):

        nums.sort()

        result = []

        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:

                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result


def main():

    nums = [-1, 0, 1, 2, -1, -4]

    solution = Solution()

    result = solution.three_sum(nums)

    print("Input:", nums)
    print("Triplets:", result)


if __name__ == "__main__":
    main()