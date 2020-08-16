from Pascal_Triangle_II___Reduce import Solution


def test1():
    s = Solution()
    rowIndex = 3
    ans = s.getRow(rowIndex)
    assert ans == [1, 3, 3, 1]


def test2():
    s = Solution()
    rowIndex = 0
    ans = s.getRow(rowIndex)
    assert ans == [1]


def test3():
    s = Solution()
    rowIndex = 1
    ans = s.getRow(rowIndex)
    assert ans == [1, 1]
