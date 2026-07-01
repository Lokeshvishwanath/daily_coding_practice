# day65_check_sorted.py

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