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


# day28_find_peak_element.py

class Solution:

    def find_peak(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:

                left = mid + 1

            else:

                right = mid

        return left


def main():

    nums = [1, 2, 3, 1]

    solution = Solution()

    peak = solution.find_peak(nums)

    print("Array:", nums)
    print("Peak Index:", peak)
    print("Peak Element:", nums[peak])


if __name__ == "__main__":
    main()