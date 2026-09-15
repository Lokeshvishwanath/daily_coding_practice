# day43_max_sum_subarray.py

class Solution:

    def max_sum_subarray(self, arr, k):

        if k > len(arr):
            return None

        window_sum = 0
        max_sum = float("-inf")

        for i in range(len(arr)):

            window_sum += arr[i]

            if i >= k - 1:

                max_sum = max(max_sum, window_sum)

                window_sum -= arr[i - k + 1]

        return max_sum


def main():

    arr = [2, 1, 5, 1, 3, 2]
    k = 3

    solution = Solution()

    result = solution.max_sum_subarray(arr, k)

    print("Array:", arr)
    print("K:", k)
    print("Maximum Sum:", result)


if __name__ == "__main__":
    main()