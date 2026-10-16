
# day60_trapping_rain_water.py

class Solution:

    def trap(self, height):

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            if height[left] <= height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water


def main():

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    solution = Solution()
    result = solution.trap(height)

    print("Heights:", height)
    print("Trapped Rain Water:", result, "units")


if __name__ == "__main__":
    main()






# day59_palindromic_substrings.py

class Solution:

    def count_substrings(self, s):

        count = 0

        def expand(left, right):

            nonlocal count

            while (
                left >= 0
                and right < len(s)
                and s[left] == s[right]
            ):
                count += 1

                left -= 1
                right += 1

        for i in range(len(s)):

            # Odd-length palindromes
            expand(i, i)

            # Even-length palindromes
            expand(i, i + 1)

        return count


def main():

    s = "aaa"

    solution = Solution()
    result = solution.count_substrings(s)

    print("Input:", s)
    print("Number of Palindromic Substrings:", result)


if __name__ == "__main__":
    main()

