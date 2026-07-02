# day66_linear_search.py

class Solution:

    def linear_search(self, arr, target):

        for i in range(len(arr)):

            if arr[i] == target:

                return i

        return -1


def main():

    arr = [15, 8, 23, 42, 16, 4]
    target = 42

    solution = Solution()

    index = solution.linear_search(arr, target)

    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()