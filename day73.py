# day14_majority_element.py

class Solution:

    def majority_element(self, arr):

        count = 0
        candidate = None

        for num in arr:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


def main():

    arr = [2, 2, 1, 2, 3, 2, 2]

    solution = Solution()

    result = solution.majority_element(arr)

    print("Array:", arr)
    print("Majority Element:", result)


if __name__ == "__main__":
    main()

# day14A_missing_number.py

class Solution:

    def find_missing(self, arr, n):

        expected_sum = n * (n + 1) // 2

        actual_sum = sum(arr)

        return expected_sum - actual_sum


def main():

    arr = [1, 2, 4, 5]

    n = 5

    solution = Solution()

    result = solution.find_missing(arr, n)

    print("Array:", arr)
    print("Missing Number:", result)


if __name__ == "__main__":
    main()