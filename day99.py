# day34A_trapping_rain_water.py

class Solution:

    def trap(self, height):

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            if height[left] <= height[right]:

                if height[left] >= left_max:
                    left_max = height[left]

                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]

                else:
                    water += right_max - height[right]

                right -= 1

        return water


def main():

    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    solution = Solution()

    result = solution.trap(height)

    print("Heights:", height)
    print("Trapped Water:", result)


if __name__ == "__main__":
    main()