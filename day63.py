# day63_second_largest.py

class Solution:

    def find_second_largest(self, arr):

        largest = float("-inf")
        second_largest = float("-inf")

        for num in arr:

            if num > largest:

                second_largest = largest
                largest = num

            elif num > second_largest and num != largest:

                second_largest = num

        if second_largest == float("-inf"):
            return "Second largest element does not exist."

        return second_largest


def main():

    arr = [12, 45, 7, 89, 23, 56]

    solution = Solution()

    result = solution.find_second_largest(arr)

    print("Array:", arr)
    print("Second Largest:", result)


if __name__ == "__main__":
    main()