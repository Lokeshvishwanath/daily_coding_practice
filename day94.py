# day30_valid_parentheses.py

class Solution:

    def is_valid(self, s):

        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:

            if char in pairs.values():

                stack.append(char)

            else:

                if not stack:
                    return False

                if stack[-1] != pairs[char]:
                    return False

                stack.pop()

        return len(stack) == 0


def main():

    s = "([{}])"

    solution = Solution()

    result = solution.is_valid(s)

    print("Input:", s)
    print("Valid Parentheses:", result)


if __name__ == "__main__":
    main()