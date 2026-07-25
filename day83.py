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

# day23A_insert_interval.py

class Solution:

    def insert_interval(self, intervals, new_interval):

        result = []

        i = 0
        n = len(intervals)

        # Add all intervals before the new interval
        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= new_interval[1]:

            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])

            i += 1

        result.append(new_interval)

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


def main():

    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]

    solution = Solution()

    result = solution.insert_interval(intervals, new_interval)

    print("Intervals    :", intervals)
    print("New Interval :", [2, 5])
    print("Result       :", result)


if __name__ == "__main__":
    main()