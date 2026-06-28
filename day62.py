# day62_smallest_element.py

class Solution:

    def find_smallest(self, arr):

        smallest = arr[0]

        for num in arr:

            if num < smallest:

                smallest = num

        return smallest


def main():

    arr = [45, 12, 78, 3, 56, 19]

    solution = Solution()

    result = solution.find_smallest(arr)

    print("Array:", arr)
    print("Smallest Element:", result)


if __name__ == "__main__":
    main()