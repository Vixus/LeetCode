from Numbers_With_Same_Consecutive_Differences import Solution


def test1():
    s = Solution()
    N = 3
    K = 7
    ans = s.numsSameConsecDiff(N, K)
    assert sorted(ans) == [181, 292, 707, 818, 929]


def test2():
    s = Solution()
    N = 2
    K = 1
    ans = s.numsSameConsecDiff(N, K)
    assert sorted(ans) == [10, 12, 21, 23, 32, 34, 43,
                           45, 54, 56, 65, 67, 76, 78, 87, 89, 98]


def test3():
    s = Solution()
    N = 1
    K = 0
    ans = s.numsSameConsecDiff(N, K)
    assert sorted(ans) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test4():
    s = Solution()
    N = 2
    K = 0
    ans = s.numsSameConsecDiff(N, K)
    assert sorted(ans) == [11, 22, 33, 44, 55, 66, 77, 88, 99]
