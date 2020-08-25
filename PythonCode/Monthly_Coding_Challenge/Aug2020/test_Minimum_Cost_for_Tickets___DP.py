from Minimum_Cost_for_Tickets___DP import Solution


def test1():
    s = Solution()
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]
    ans = s.mincostTickets(days, costs)
    assert ans == 11


def test2():
    s = Solution()
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    ans = s.mincostTickets(days, costs)
    assert ans == 17
