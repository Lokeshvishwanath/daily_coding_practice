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


# day30A_min_stack.py

class MinStack:

    def __init__(self):

        self.stack = []
        self.min_stack = []

    def push(self, value):

        self.stack.append(value)

        if not self.min_stack:
            self.min_stack.append(value)

        else:
            current_min = min(value, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self):

        if not self.stack:
            return None

        self.min_stack.pop()

        return self.stack.pop()

    def top(self):

        if not self.stack:
            return None

        return self.stack[-1]

    def get_min(self):

        if not self.min_stack:
            return None

        return self.min_stack[-1]


def main():

    stack = MinStack()

    stack.push(5)
    stack.push(3)
    stack.push(7)
    stack.push(2)

    print("Stack:", stack.stack)
    print("Top:", stack.top())
    print("Minimum:", stack.get_min())

    stack.pop()

    print("\nAfter pop:")
    print("Stack:", stack.stack)
    print("Top:", stack.top())
    print("Minimum:", stack.get_min())


if __name__ == "__main__":
    main()