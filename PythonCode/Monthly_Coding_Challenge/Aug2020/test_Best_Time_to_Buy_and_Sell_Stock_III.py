from Best_Time_to_Buy_and_Sell_Stock_III import Solution


def test1():
    s = Solution()
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    ans = s.maxProfit(prices)
    assert ans == 6


def test2():
    s = Solution()
    prices = [1, 2, 3, 4, 5]
    ans = s.maxProfit(prices)
    assert ans == 4


def test3():
    s = Solution()
    prices = [7, 6, 4, 3, 1]
    ans = s.maxProfit(prices)
    assert ans == 0
