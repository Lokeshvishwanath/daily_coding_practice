# day20_longest_consecutive_sequence.py

class Solution:

    def longest_consecutive(self, nums):

        if not nums:
            return 0

        num_set = set(nums)

        longest = 0

        for num in num_set:

            # Start only if it is the beginning of a sequence
            if num - 1 not in num_set:

                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


def main():

    nums = [100, 4, 200, 1, 3, 2]

    solution = Solution()

    result = solution.longest_consecutive(nums)

    print("Array :", nums)
    print("Longest Consecutive Length:", result)


if __name__ == "__main__":
    main()