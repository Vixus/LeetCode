from CountSquareSubmatricesWithAllOnes import Solution


def test1():
    s = Solution()
    matrix = [[0, 1, 1, 1],
              [1, 1, 1, 1],
              [0, 1, 1, 1]
              ]
    ans = s.countSquares(matrix)
    assert ans == 15


def test2():
    s = Solution()
    matrix = [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
    ans = s.countSquares(matrix)
    assert ans == 7
