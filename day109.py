# day42_permutation_in_string.py

class Solution:

    def check_inclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        count_window = [0] * 26

        for char in s1:
            index = ord(char) - ord('a')
            count_s1[index] += 1

        window_size = len(s1)

        for i in range(window_size):
            index = ord(s2[i]) - ord('a')
            count_window[index] += 1

        if count_s1 == count_window:
            return True

        for right in range(window_size, len(s2)):

            # Add new character
            new_index = ord(s2[right]) - ord('a')
            count_window[new_index] += 1

            # Remove old character
            left = right - window_size
            old_index = ord(s2[left]) - ord('a')
            count_window[old_index] -= 1

            if count_s1 == count_window:
                return True

        return False


def main():

    s1 = "ab"
    s2 = "eidbaooo"

    solution = Solution()

    result = solution.check_inclusion(s1, s2)

    print("s1:", s1)
    print("s2:", s2)
    print("Permutation Found:", result)


if __name__ == "__main__":
    main()