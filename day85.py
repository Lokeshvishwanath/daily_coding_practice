# day24_meeting_rooms.py

class Solution:

    def can_attend_meetings(self, intervals):

        intervals.sort()

        for i in range(1, len(intervals)):

            previous_end = intervals[i - 1][1]
            current_start = intervals[i][0]

            if current_start < previous_end:
                return False

        return True


def main():

    intervals = [[0, 30], [35, 40], [45, 50]]

    solution = Solution()

    result = solution.can_attend_meetings(intervals)

    print("Meetings:", intervals)
    print("Can Attend All Meetings:", result)


if __name__ == "__main__":
    main()