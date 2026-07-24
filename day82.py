

import heapq


class Solution:

    def top_k_frequent(self, nums, k):

        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        result = heapq.nlargest(k, frequency, key=frequency.get)

        return result


def main():

    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    solution = Solution()

    result = solution.top_k_frequent(nums, k)

    print("Array :", nums)
    print("Top", k, "Frequent Elements:", result)


if __name__ == "__main__":
    main()