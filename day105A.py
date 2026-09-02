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