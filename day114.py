# day48_minimum_window_substring.py

class Solution:

    def min_window(self, s, t):

        if not s or not t:
            return ""

        required = {}

        for char in t:
            required[char] = required.get(char, 0) + 1

        window = {}

        left = 0

        formed = 0
        required_count = len(required)

        min_length = float("inf")
        min_left = 0

        for right in range(len(s)):

            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in required and window[char] == required[char]:
                formed += 1

            while formed == required_count:

                current_length = right - left + 1

                if current_length < min_length:
                    min_length = current_length
                    min_left = left

                left_char = s[left]

                window[left_char] -= 1

                if (
                    left_char in required
                    and window[left_char] < required[left_char]
                ):
                    formed -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_left:min_left + min_length]


def main():

    s = "ADOBECODEBANC"
    t = "ABC"

    solution = Solution()

    result = solution.min_window(s, t)

    print("String:", s)
    print("Target:", t)
    print("Minimum Window:", result)


if __name__ == "__main__":
    main()