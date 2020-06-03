from typing import List
from collections import Counter


class StockSpanner:
    """
    Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
    The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
    For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].
    """

    def __init__(self):
        self.monotone_stack = []

    def next(self, price: int) -> int:
        stack = self.monotone_stack
        cur_price_quote, cur_price_span = price, 1

        # Compute price span in stock data with monotonic stack
        while stack and stack[-1][0] <= cur_price_quote:

            prev_price_quote, prev_price_span = stack.pop()

            # update current price span with history data in stack
            cur_price_span += prev_price_span

        # Update latest price quote and price span
        stack.append((cur_price_quote, cur_price_span))

        return cur_price_span
        # Your StockSpanner object will be instantiated and called as such:
        # obj = StockSpanner()
        # param_1 = obj.next(price)


def main():
    ansArr = []
    stockPriceArr = [100, 80, 60, 70, 60, 75, 85]
    obj = StockSpanner()
    for x in stockPriceArr:
        ansArr.append(obj.next(x))

    print(ansArr)


if __name__ == '__main__':
    main()
