from FloodFill import Solution


def test1():
    s = Solution()
    ans = s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    assert ans == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]


def test2():
    s = Solution()
    ans = s.floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1)
    assert ans == [[0, 0, 0], [0, 1, 1]]
