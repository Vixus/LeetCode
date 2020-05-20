from typing import List
from collections import Counter


class StockSpanner:

    def __init__(self):
        self.priceArr = []
        self.stockSpannerArr = []

    def next(self, price: int) -> int:
        len_s = len(self.priceArr)
        dayCount = 1

        i = len_s-1
        while i >= 0:
            if price >= self.priceArr[i]:
                dayCount += self.stockSpannerArr[i]
                i -= self.stockSpannerArr[i]
            else:
                break

        self.priceArr.append(price)
        self.stockSpannerArr.append(dayCount)
        return dayCount
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
