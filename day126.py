
# day58_longest_palindromic_substring.py

class Solution:

    def expand(self, s, left, right):

        while (
            left >= 0
            and right < len(s)
            and s[left] == s[right]
        ):
            left -= 1
            right += 1

        return left + 1, right - 1

    def longest_palindrome(self, s):

        if not s:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):

            # Odd-length palindrome
            left1, right1 = self.expand(s, i, i)

            # Even-length palindrome
            left2, right2 = self.expand(s, i, i + 1)

            if right1 - left1 > end - start:
                start = left1
                end = right1

            if right2 - left2 > end - start:
                start = left2
                end = right2

        return s[start:end + 1]


def main():

    s = "babad"

    solution = Solution()
    result = solution.longest_palindrome(s)

    print("Input:", s)
    print("Longest Palindromic Substring:", result)


if __name__ == "__main__":
    main()
