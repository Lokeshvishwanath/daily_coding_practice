# day34_largest_rectangle_histogram.py

class Solution:

    def largest_rectangle(self, heights):

        stack = []
        max_area = 0

        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                height_index = stack.pop()

                height = heights[height_index]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width

                max_area = max(max_area, area)

            stack.append(i)

        return max_area


def main():

    heights = [2, 1, 5, 6, 2, 3]

    solution = Solution()

    result = solution.largest_rectangle(heights)

    print("Heights:", heights[:-1])
    print("Largest Rectangle Area:", result)


if __name__ == "__main__":
    main()