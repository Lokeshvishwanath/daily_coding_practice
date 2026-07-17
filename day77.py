# day17_merge_sorted_arrays.py

class Solution:

    def merge_arrays(self, arr1, arr2):

        result = []

        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):

            if arr1[i] <= arr2[j]:

                result.append(arr1[i])
                i += 1

            else:

                result.append(arr2[j])
                j += 1

        while i < len(arr1):

            result.append(arr1[i])
            i += 1

        while j < len(arr2):

            result.append(arr2[j])
            j += 1

        return result


def main():

    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]

    solution = Solution()

    merged = solution.merge_arrays(arr1, arr2)

    print("Array 1:", arr1)
    print("Array 2:", arr2)
    print("Merged Array:", merged)


if __name__ == "__main__":
    main()

# day17A_move_zeroes.py

class Solution:

    def move_zeroes(self, arr):

        left = 0

        for right in range(len(arr)):

            if arr[right] != 0:

                arr[left], arr[right] = arr[right], arr[left]

                left += 1

        return arr


def main():

    arr = [0, 1, 0, 3, 12]

    solution = Solution()

    result = solution.move_zeroes(arr)

    print("Original Array :", [0, 1, 0, 3, 12])
    print("Modified Array :", result)


if __name__ == "__main__":
    main()