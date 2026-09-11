# day41_longest_repeating_character_replacement.py

class Solution:

    def character_replacement(self, s, k):

        count = {}

        left = 0
        max_frequency = 0
        max_length = 0

        for right in range(len(s)):

            char = s[right]

            count[char] = count.get(char, 0) + 1

            max_frequency = max(max_frequency, count[char])

            window_length = right - left + 1

            replacements = window_length - max_frequency

            while replacements > k:

                count[s[left]] -= 1

                left += 1

                window_length = right - left + 1
                replacements = window_length - max_frequency

            max_length = max(max_length, window_length)

        return max_length


def main():

    s = "AABABBA"
    k = 1

    solution = Solution()

    result = solution.character_replacement(s, k)

    print("String:", s)
    print("K:", k)
    print("Longest Length:", result)


if __name__ == "__main__":
    main()