# day18_best_time_to_buy_sell_stock.py

class Solution:

    def max_profit(self, prices):

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:

            if price < min_price:
                min_price = price

            else:
                profit = price - min_price

                if profit > max_profit:
                    max_profit = profit

        return max_profit


def main():

    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()

    result = solution.max_profit(prices)

    print("Stock Prices :", prices)
    print("Maximum Profit:", result)


if __name__ == "__main__":
    main()

# day18A_product_of_array_except_self

class Solution:

    def product_except_self(self, nums):

        n = len(nums)

        answer = [1] * n

        prefix = 1

        for i in range(n):

            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(n - 1, -1, -1):

            answer[i] *= suffix
            suffix *= nums[i]

        return answer


def main():

    nums = [1, 2, 3, 4]

    solution = Solution()

    result = solution.product_except_self(nums)

    print("Input :", nums)
    print("Output:", result)


if __name__ == "__main__":
    main()