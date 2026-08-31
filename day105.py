# day37_valid_palindrome.py

class Solution:

    def is_palindrome(self, s):

        cleaned = ""

        for char in s:

            if char.isalnum():
                cleaned += char.lower()

        left = 0
        right = len(cleaned) - 1

        while left < right:

            if cleaned[left] != cleaned[right]:
                return False

            left += 1
            right -= 1

        return True


def main():

    s = "A man, a plan, a canal: Panama"

    solution = Solution()

    result = solution.is_palindrome(s)

    print("String:", s)
    print("Is Palindrome:", result)


if __name__ == "__main__":
    main()