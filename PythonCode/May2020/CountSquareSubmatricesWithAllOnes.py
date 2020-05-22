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
        mat = np.array(matrix)
        count = 0
        N = len(mat)
        M = len(mat[0])
        max_k = max(M, N)

        for i in range(N):
            for j in range(M):
                for k in range(1, min(max_k, min(N-i, M-j))+1):
                    subMatrix = mat[i:i+k, j:j+k]
                    sumMatrix = subMatrix.sum()
                    print(subMatrix)
                    if sumMatrix == k**2:
                        count += 1
                    else:
                        break

        return count


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
