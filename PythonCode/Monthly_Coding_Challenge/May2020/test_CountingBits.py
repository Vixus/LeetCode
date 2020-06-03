from CountingBits import Solution


def test1():
    s = Solution()
    N = 2
    ans = s.countBits(N)
    assert ans == [0, 1, 1]


def test2():
    s = Solution()
    N = 5
    ans = s.countBits(N)
    assert ans == [0, 1, 1, 2, 1, 2]


def test3():
    s = Solution()
    N = 15
    ans = s.countBits(N)
    assert ans == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
