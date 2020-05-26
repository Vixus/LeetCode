from UncrossedLines import Solution


def test1():
    s = Solution()
    A = [1, 4, 2]
    B = [1, 2, 4]
    ans = s.maxUncrossedLines(A, B)
    assert ans == 2


def test2():
    s = Solution()
    A = [2, 5, 1, 2, 5]
    B = [10, 5, 2, 1, 5, 2]
    ans = s.maxUncrossedLines(A, B)
    assert ans == 3


def test3():
    s = Solution()
    A = [1, 3, 7, 1, 7, 5]
    B = [1, 9, 2, 5, 1]
    ans = s.maxUncrossedLines(A, B)
    assert ans == 2
