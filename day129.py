
# day62_daily_temperatures.py

class Solution:

    def daily_temperatures(self, temperatures):

        n = len(temperatures)

        answer = [0] * n
        stack = []

        for i in range(n):

            while (
                stack
                and temperatures[i] > temperatures[stack[-1]]
            ):
                previous_day = stack.pop()

                answer[previous_day] = i - previous_day

            stack.append(i)

        return answer


def main():

    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    solution = Solution()
    result = solution.daily_temperatures(temperatures)

    print("Temperatures:", temperatures)
    print("Days to Wait:", result)


if __name__ == "__main__":
    main()
