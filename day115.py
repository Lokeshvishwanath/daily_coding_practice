# day49_product_except_self.py

class Solution:

    def product_except_self(self, nums):

        n = len(nums)

        answer = [1] * n

        # Prefix products
        prefix_product = 1

        for i in range(n):

            answer[i] = prefix_product

            prefix_product *= nums[i]

        # Suffix products
        suffix_product = 1

        for i in range(n - 1, -1, -1):

            answer[i] *= suffix_product

            suffix_product *= nums[i]

        return answer


def main():

    nums = [1, 2, 3, 4]

    solution = Solution()

    result = solution.product_except_self(nums)

    print("Input:", nums)
    print("Output:", result)


if __name__ == "__main__":
    main()