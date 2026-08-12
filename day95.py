# day31_next_greater_element.py

class Solution:

    def next_greater(self, arr):

        result = [-1] * len(arr)
        stack = []

        for i in range(len(arr) - 1, -1, -1):

            while stack and stack[-1] <= arr[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1]

            stack.append(arr[i])

        return result


def main():

    arr = [4, 5, 2, 10, 8]

    solution = Solution()

    result = solution.next_greater(arr)

    print("Array:", arr)
    print("Next Greater Elements:", result)


if __name__ == "__main__":
    main()


# day31A_daily_temperatures.py

class Solution:

    def daily_temperatures(self, temperatures):

        result = [0] * len(temperatures)

        stack = []

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:

                previous_day = stack.pop()

                result[previous_day] = i - previous_day

            stack.append(i)

        return result


def main():

    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

    solution = Solution()

    result = solution.daily_temperatures(temperatures)

    print("Temperatures:", temperatures)
    print("Days to Wait:", result)


if __name__ == "__main__":
    main()