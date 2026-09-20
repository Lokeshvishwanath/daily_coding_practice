# day47_find_all_anagrams.py

class Solution:

    def find_anagrams(self, s, p):

        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window_count = [0] * 26

        result = []

        # Count characters in p
        for char in p:
            index = ord(char) - ord('a')
            p_count[index] += 1

        window_size = len(p)

        # Create first window
        for i in range(window_size):
            index = ord(s[i]) - ord('a')
            window_count[index] += 1

        # Check first window
        if p_count == window_count:
            result.append(0)

        # Slide the window
        for right in range(window_size, len(s)):

            # Add new character
            new_index = ord(s[right]) - ord('a')
            window_count[new_index] += 1

            # Remove old character
            left = right - window_size
            old_index = ord(s[left]) - ord('a')
            window_count[old_index] -= 1

            # Check current window
            if p_count == window_count:
                result.append(left + 1)

        return result


def main():

    s = "cbaebabacd"
    p = "abc"

    solution = Solution()

    result = solution.find_anagrams(s, p)

    print("String:", s)
    print("Pattern:", p)
    print("Anagram Indices:", result)


if __name__ == "__main__":
    main()