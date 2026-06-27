# Day 61 - Find the Largest Number in a List

class Solution:

    def find_largest(self, numbers):

        largest = numbers[0]

        for number in numbers:

            if number > largest:

                largest = number

        return largest


def main():

    numbers = [12, 45, 7, 89, 23, 56]

    solution = Solution()

    result = solution.find_largest(numbers)

    print("Numbers :", numbers)
    print("Largest :", result)


if __name__ == "__main__":
    main()