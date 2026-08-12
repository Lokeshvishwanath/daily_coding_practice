# day31_next_greater_element.py

class Solution:

    def next_greater(self, arr):

        result = [-1] * len(arr)
        stack = []

        for i in range(len(arr) - 1, -1, -1):

            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(arr[i])

        return result


def main():

    arr = [4, 5, 2, 10, 8]

    solution = Solution()

    result = solution.next_greater(arr)

    print("Array:", arr)
    print("Next Greater Elements:", result)


if __name__ == "__main__":
    main()