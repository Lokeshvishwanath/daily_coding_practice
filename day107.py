class Solution:

    def longest_substring(self, s):

        char_set = set()

        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            length = right - left + 1

            max_length = max(max_length, length)

        return max_length


def main():

    s = "abcabcbb"

    solution = Solution()

    result = solution.longest_substring(s)

    print("String:", s)
    print("Longest Length:", result)


if __name__ == "__main__":
    main()