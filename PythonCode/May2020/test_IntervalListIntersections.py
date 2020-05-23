from IntervalListIntersections import Solution


def test1():
    s = Solution()
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    ans = s.intervalIntersection(A, B)
    assert ans == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]


def test2():
    s = Solution()
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    ans = s.intervalIntersection(A, B)
    assert ans == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]


def test3():
    s = Solution()
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    ans = s.intervalIntersection(A, B)
    assert ans == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
