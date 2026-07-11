# day13_move_zeros_to_end.py

class Solution:

    def move_zeros(self, arr):

        j = 0

        for i in range(len(arr)):

            if arr[i] != 0:

                arr[j], arr[i] = arr[i], arr[j]
                j += 1

        return arr


def main():

    arr = [0, 1, 0, 3, 12, 0, 5]

    solution = Solution()

    result = solution.move_zeros(arr)

    print("Original Array: [0, 1, 0, 3, 12, 0, 5]")
    print("After Moving Zeros:", result)


if __name__ == "__main__":
    main()