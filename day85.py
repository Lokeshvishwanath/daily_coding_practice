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

# day24A_meeting_rooms_2.py

import heapq


class Solution:

    def min_meeting_rooms(self, intervals):

        if not intervals:
            return 0

        intervals.sort()

        min_heap = []

        heapq.heappush(min_heap, intervals[0][1])

        for i in range(1, len(intervals)):

            start = intervals[i][0]
            end = intervals[i][1]

            if start >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

        return len(min_heap)


def main():

    intervals = [[0, 30], [5, 10], [15, 20]]

    solution = Solution()

    rooms = solution.min_meeting_rooms(intervals)

    print("Meetings:", intervals)
    print("Minimum Rooms Required:", rooms)


if __name__ == "__main__":
    main()