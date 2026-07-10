# day11_right_rotate_array.py

class Solution:

    def right_rotate(self, arr):

        if len(arr) == 0:
            return arr

        last_element = arr[-1]

        for i in range(len(arr) - 1, 0, -1):

            arr[i] = arr[i - 1]

        arr[0] = last_element

        return arr


def main():

    arr = [10, 20, 30, 40, 50]

    solution = Solution()

    result = solution.right_rotate(arr)

    print("Original Array: [10, 20, 30, 40, 50]")
    print("Right Rotated Array:", result)


if __name__ == "__main__":
    main()