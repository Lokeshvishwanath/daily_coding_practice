# day33_evaluate_reverse_polish_notation.py

class Solution:

    def evaluate(self, tokens):

        stack = []

        for token in tokens:

            if token not in {"+", "-", "*", "/"}:

                stack.append(int(token))

            else:

                second = stack.pop()
                first = stack.pop()

                if token == "+":
                    result = first + second

                elif token == "-":
                    result = first - second

                elif token == "*":
                    result = first * second

                else:
                    result = int(first / second)

                stack.append(result)

        return stack[-1]


def main():

    tokens = ["2", "1", "+", "3", "*"]

    solution = Solution()

    result = solution.evaluate(tokens)

    print("Expression:", tokens)
    print("Result:", result)


if __name__ == "__main__":
    main()