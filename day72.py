# day13_move_zeros_to_end.py

class Solution:

    def move_zeros(self, arr):

        j = 0

        for i in range(len(arr)):

            if arr[i] != 0:

                arr[j], arr[i] = arr[i], arr[j]
                j += 1

        return arr


def main():

    arr = [0, 1, 0, 3, 12, 0, 5]

    solution = Solution()

    result = solution.move_zeros(arr)

    print("Original Array: [0, 1, 0, 3, 12, 0, 5]")
    print("After Moving Zeros:", result)


if __name__ == "__main__":
    main()


# day13_leader_elements.py

class Solution:

    def find_leaders(self, arr):

        leaders = []

        max_from_right = arr[-1]

        leaders.append(max_from_right)

        for i in range(len(arr) - 2, -1, -1):

            if arr[i] > max_from_right:

                leaders.append(arr[i])
                max_from_right = arr[i]

        leaders.reverse()

        return leaders


def main():

    arr = [16, 17, 4, 3, 5, 2]

    solution = Solution()

    result = solution.find_leaders(arr)

    print("Array:", arr)
    print("Leader Elements:", result)


if __name__ == "__main__":
    main()