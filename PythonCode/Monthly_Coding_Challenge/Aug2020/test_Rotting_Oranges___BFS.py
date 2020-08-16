from Rotting_Oranges___BFS import Solution


def test1():
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    ans = s.orangesRotting(grid)
    assert ans == 4


def test2():
    s = Solution()
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    ans = s.orangesRotting(grid)
    assert ans == -1


def test3():
    s = Solution()
    grid = [[0, 2]]
    ans = s.orangesRotting(grid)
    assert ans == 0


def test4():
    s = Solution()
    grid = [[0]]
    ans = s.orangesRotting(grid)
    assert ans == 0


def test5():
    s = Solution()
    grid = [[1, 1, 1]]
    ans = s.orangesRotting(grid)
    assert ans == -1
