# day09_remove_duplicates.py

class Solution:

    def remove_duplicates(self, arr):

        if len(arr) == 0:
            return []

        i = 0

        for j in range(1, len(arr)):

            if arr[i] != arr[j]:

                i += 1
                arr[i] = arr[j]

        return arr[:i + 1]


def main():

    arr = [1, 1, 2, 2, 3, 4, 4, 5]

    solution = Solution()

    result = solution.remove_duplicates(arr)

    print("Original Array:", arr)
    print("Array After Removing Duplicates:", result)


if __name__ == "__main__":
    main()