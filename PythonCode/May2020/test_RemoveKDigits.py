from RemoveKDigits import Solution


def test1():
    s = Solution()
    ans = s.removeKdigits(1432219, 3)
    assert ans == 1219


def test2():
    s = Solution()
    ans = s.removeKdigits(10200, 1)
    assert ans == 200


def test3():
    s = Solution()
    ans = s.removeKdigits(10, 2)
    assert ans == 0
