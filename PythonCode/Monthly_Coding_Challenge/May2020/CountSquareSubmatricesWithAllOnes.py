import numpy as np
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

        Arguments:
            matrix {List[List[int]]} -- [description]

        Returns:
            int -- [description]
        """
        # mat = np.array(matrix)
        # count = 0
        # N = len(mat)
        # M = len(mat[0])
        # max_k = max(M, N)

        # for i in range(N):
        #     for j in range(M):
        #         for k in range(1, min(max_k, min(N-i, M-j))+1):
        #             subMatrix = mat[i:i+k, j:j+k]
        #             sumMatrix = subMatrix.sum()
        #             print(subMatrix)
        #             if sumMatrix == k**2:
        #                 count += 1
        #             else:
        #                 break

        # return count

        if matrix is None or len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:  # Cases with first row or first col
                        result += 1  # The 1 cells are square on its own
                    else:  # Other cells
                        cell_val = min(
                            matrix[r-1][c-1], matrix[r][c-1], matrix[r-1][c]) + matrix[r][c]
                        result += cell_val
                        # **memoize the updated result**
                        matrix[r][c] = cell_val
        return result


def main():
    s = Solution()
    matrix = [[1, 1],
              [0, 0],
              [1, 1]
              ]
    ans = s.countSquares(matrix)
    print(ans)


if __name__ == '__main__':
    main()
