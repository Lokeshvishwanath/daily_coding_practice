# day23_merge_intervals.py

class Solution:

    def merge_intervals(self, intervals):

        # Sort intervals based on the starting value
        intervals.sort()

        merged = []

        for interval in intervals:

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)

            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


def main():

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

    solution = Solution()

    result = solution.merge_intervals(intervals)

    print("Input Intervals :", intervals)
    print("Merged Intervals:", result)


if __name__ == "__main__":
    main()