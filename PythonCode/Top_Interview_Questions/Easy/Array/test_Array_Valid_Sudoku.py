from Array_Valid_Sudoku import Solution


def test1():
    s = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    ans = s.isValidSudoku(board)

    assert ans == True


def test2():
    s = Solution()
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    ans = s.isValidSudoku(board)

    assert ans == False


def test3():
    s = Solution()
    board = [
        [".", ".", ".", "9", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["1", ".", ".", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", ".", "2", ".", "6", ".", "."],
        [".", "9", ".", ".", ".", ".", ".", "7", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["8", ".", ".", "8", ".", ".", ".", ".", "."]
    ]
    ans = s.isValidSudoku(board)

    assert ans == False