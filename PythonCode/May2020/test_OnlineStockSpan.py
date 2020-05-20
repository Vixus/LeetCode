from OnlineStockSpan import StockSpanner


def test1():
    s = StockSpanner()
    ans = []
    stockPriceArr = [100, 80, 60, 70, 60, 75, 85]
    for x in stockPriceArr:
        ans.append(s.next(x))
    assert ans == [1, 1, 1, 2, 1, 4, 6]
