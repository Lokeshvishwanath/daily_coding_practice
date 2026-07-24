

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


# day22A_kth_largest_element.py

import heapq


class Solution:

    def find_kth_largest(self, nums, k):

        min_heap = nums[:k]

        heapq.heapify(min_heap)

        for num in nums[k:]:

            if num > min_heap[0]:

                heapq.heappop(min_heap)

                heapq.heappush(min_heap, num)

        return min_heap[0]


def main():

    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    solution = Solution()

    result = solution.find_kth_largest(nums, k)

    print("Array :", nums)
    print("k =", k)
    print("Kth Largest Element:", result)


if __name__ == "__main__":
    main()