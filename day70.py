# day10_left_rotate_array.py

class Solution:

    def left_rotate(self, arr):

        if len(arr) == 0:
            return arr

        first_element = arr[0]

        for i in range(len(arr) - 1):

            arr[i] = arr[i + 1]

        arr[-1] = first_element

        return arr


def main():

    arr = [10, 20, 30, 40, 50]

    solution = Solution()

    result = solution.left_rotate(arr)

    print("Original Array: [10, 20, 30, 40, 50]")
    print("Left Rotated Array:", result)


if __name__ == "__main__":
    main()

    # day05_check_sorted.py

class Solution:

    def is_sorted(self, arr):

        for i in range(len(arr) - 1):

            if arr[i] > arr[i + 1]:

                return False

        return True


def main():

    arr = [10, 20, 30, 40, 50]

    solution = Solution()

    if solution.is_sorted(arr):
        print("Array is Sorted")
    else:
        print("Array is Not Sorted")


if __name__ == "__main__":
    main()