# day52_best_time_to_buy_sell_stock.py

class Solution:

    def max_profit(self, prices):

        minimum_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < minimum_price:
                minimum_price = price

            profit = price - minimum_price

            if profit > max_profit:
                max_profit = profit

        return max_profit


def main():

    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()

    result = solution.max_profit(prices)

    print("Prices:", prices)
    print("Maximum Profit:", result)


if __name__ == "__main__":
    main()