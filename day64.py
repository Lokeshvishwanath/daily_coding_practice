# day64_reverse_array.py

class Solution:

    def reverse_array(self, arr):

        left = 0
        right = len(arr) - 1

        while left < right:

            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        return arr


def main():

    arr = [10, 20, 30, 40, 50]

    solution = Solution()

    result = solution.reverse_array(arr)

    print("Reversed Array:", result)


if __name__ == "__main__":
    main()