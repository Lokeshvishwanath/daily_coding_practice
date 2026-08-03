# day27_search_insert_position.py

class Solution:

    def search_insert(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return left


def main():

    nums = [1, 3, 5, 6]
    target = 2

    solution = Solution()

    result = solution.search_insert(nums, target)

    print("Array :", nums)
    print("Target:", target)
    print("Insert Position:", result)


if __name__ == "__main__":
    main()


# day27A_square_root.py

class Solution:

    def my_sqrt(self, x):

        if x == 0 or x == 1:
            return x

        left = 1
        right = x
        answer = 0

        while left <= right:

            mid = (left + right) // 2

            square = mid * mid

            if square == x:
                return mid

            elif square < x:

                answer = mid
                left = mid + 1

            else:

                right = mid - 1

        return answer


def main():

    x = 20

    solution = Solution()

    result = solution.my_sqrt(x)

    print("Number:", x)
    print("Square Root:", result)


if __name__ == "__main__":
    main()