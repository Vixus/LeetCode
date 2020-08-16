from Non_Overlapping_Intervals import Solution


def test1():
    s = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    ans = s.eraseOverlapIntervals(intervals)
    assert ans == 1


def test2():
    s = Solution()
    intervals = [[1, 2], [1, 2], [1, 2]]
    ans = s.eraseOverlapIntervals(intervals)
    assert ans == 2


def test3():
    s = Solution()
    intervals = [[1, 2], [2, 3]]
    ans = s.eraseOverlapIntervals(intervals)
    assert ans == 0


def test4():
    s = Solution()
    intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
    ans = s.eraseOverlapIntervals(intervals)
    assert ans == 2


def test5():
    s = Solution()
    intervals = [[1, 2], [2, 3], [3, 4], [-100, -2], [5, 7]]
    ans = s.eraseOverlapIntervals(intervals)
    assert ans == 0
