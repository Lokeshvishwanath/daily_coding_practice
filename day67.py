# day67_count_even_odd.py

class Solution:

    def count_even_odd(self, arr):

        even_count = 0
        odd_count = 0

        for num in arr:

            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return even_count, odd_count


def main():

    arr = [10, 15, 22, 7, 8, 13, 40]

    solution = Solution()

    even, odd = solution.count_even_odd(arr)

    print("Array:", arr)
    print("Even Numbers:", even)
    print("Odd Numbers:", odd)


if __name__ == "__main__":
    main()