# day15_two_sum.py

class Solution:

    def two_sum(self, arr, target):

        for i in range(len(arr)):

            for j in range(i + 1, len(arr)):

                if arr[i] + arr[j] == target:

                    return [i, j]

        return []


def main():

    arr = [2, 7, 11, 15]
    target = 9

    solution = Solution()

    result = solution.two_sum(arr, target)

    print("Array :", arr)
    print("Target:", target)
    print("Indices:", result)


if __name__ == "__main__":
    main()