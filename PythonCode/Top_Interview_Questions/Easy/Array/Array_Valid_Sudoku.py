from typing import List
from collections import defaultdict
from collections import Counter
import numpy as np


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

        Args:
            board (List[List[str]]): [description]

        Returns:
            bool: [description]
        """
        m = np.matrix(board)
        rowDict = defaultdict(list)
        colDict = defaultdict(list)
        sqDict = defaultdict(list)

        # Check row, col and square index for each number
        for i in range(9):
            for j in range(9):
                if m[i, j] != '.':
                    if i in rowDict[m[i, j]] or j in colDict[m[i, j]] or (i//3*3 + j//3) in sqDict[m[i, j]]:
                        return False
                    else:
                        rowDict[m[i, j]].append(i)
                        colDict[m[i, j]].append(j)
                        sqDict[m[i, j]].append(i//3*3 + j//3)

        return True

        # seen = sum(([(i, ch), (ch, j), (i // 3, ch, j // 3)]
        #          for i, r in enumerate(board) for j, ch in enumerate(r) if ch != "."), [])

        # return len(seen) == len(set(seen))


def main():
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
    print(ans)


if __name__ == '__main__':
    main()
