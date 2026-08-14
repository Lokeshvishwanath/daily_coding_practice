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


# day32_stock_span.py

class Solution:

    def calculate_span(self, prices):

        span = [0] * len(prices)

        stack = []

        for i in range(len(prices)):

            while stack and prices[stack[-1]] <= prices[i]:
                stack.pop()

            if not stack:
                span[i] = i + 1

            else:
                span[i] = i - stack[-1]

            stack.append(i)

        return span


def main():

    prices = [100, 80, 60, 70, 60, 75, 85]

    solution = Solution()

    result = solution.calculate_span(prices)

    print("Stock Prices:", prices)
    print("Stock Span:", result)


if __name__ == "__main__":
    main()