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