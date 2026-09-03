class Solution:

    def max_area(self, heights):

        left = 0
        right = len(heights) - 1

        max_water = 0

        while left < right:

            height = min(heights[left], heights[right])
            width = right - left

            area = height * width

            max_water = max(max_water, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water


def main():

    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    solution = Solution()

    result = solution.max_area(heights)

    print("Heights:", heights)
    print("Maximum Water:", result)


if __name__ == "__main__":
    main()