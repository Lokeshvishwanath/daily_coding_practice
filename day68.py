# day68_maximum_difference.py

class Solution:

    def find_max_difference(self, arr):

        min_element = arr[0]
        max_difference = arr[1] - arr[0]

        for i in range(1, len(arr)):

            difference = arr[i] - min_element

            if difference > max_difference:
                max_difference = difference

            if arr[i] < min_element:
                min_element = arr[i]

        return max_difference


def main():

    arr = [7, 1, 5, 4, 9, 2]

    solution = Solution()

    result = solution.find_max_difference(arr)

    print("Array:", arr)
    print("Maximum Difference:", result)


if __name__ == "__main__":
    main()